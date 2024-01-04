import multiprocessing
import queue
import ctypes
import threading
import time
import cv2
import numpy as np

from aolesrtc.aolesrtc import Controller, DataIOFactory, DataIOType_AUDIO, DataIOType_I420, DataOutput, P2PClientDataIO, P2PModuleObserver, UINT8Vector

global last_id

def GetData(c_voidptr, length):
    c_void_p_obj = ctypes.c_void_p(int(c_voidptr))
    pointer_arr = ctypes.cast(c_void_p_obj, ctypes.POINTER(ctypes.c_ubyte * length))
    return pointer_arr.contents

class PythonAudioSink(DataOutput):
    def OnDataAudioOut(self, audio_data, bits_per_sample, sample_rate, number_of_channels, number_of_frames):
        print('OnDataAudioOut:', number_of_frames)
class PythonVideoSink(DataOutput):
    yuv_file = None
    vframe_queue = queue.Queue()

    def __init__(self, type):
        super().__init__(type)
        self.yuv_file = open("./out.yuv", "wb")
        

    def OnDataYUVOut(self, id, width, height, data_y, stride_y, data_u, stride_u, data_v, stride_v):
        print('OnDataYUVOut:', width , height)

        yuv = GetData(data_y, width*height*3//2)

        # self.yuv_file.write(yuv) # save recved
        # return

        yuv_data = np.frombuffer(yuv, dtype=np.uint8)
        yuv_data = yuv_data.reshape((height*3//2, width))

        rgb_image = np.zeros((height, width, 3), dtype=np.uint8)
        cv2.cvtColor(yuv_data, cv2.COLOR_YUV2BGR_I420, rgb_image)
        self.vframe_queue.put(rgb_image)
        # cv2.imwrite('./output.png', self.rgb_image)
        


class PythonP2PModuleObserver(P2PModuleObserver):
    def OnConnEvent(self, ok):
        print('OnConnEvent:', ok)

    def OnLoginEvent(self, ok, id):
        print("reset last_id of this process :", id)
        global last_id
        last_id = id
        print('OnLoginEvent:', ok, id)

def CreatePeer(is_sender, is_receiver):
    controller = Controller()
    controller.thisown = False
    time.sleep(1)
    p2p_client = P2PClientDataIO(controller)
    p2p_observer = PythonP2PModuleObserver()
    p2p_client.AddP2PModuleObserver(p2p_observer)

    dataiofactory = DataIOFactory(controller)

    if is_sender: 
        asource = dataiofactory.CreateDataIOSource(DataIOType_AUDIO)
        # asource = None # use microphone
        p2p_client.AddLocalAudioSource("audio", asource)

        vsource = dataiofactory.CreateDataIOSource(DataIOType_I420)
        p2p_client.AddLocalVideoSource("video", vsource)

        p2p_client.Login()
        return {"p2p_client" :p2p_client, "audio_source":asource, "video_source":vsource, "p2p_observer": p2p_observer}
    if is_receiver:
        py_asink = PythonAudioSink(DataIOType_AUDIO)
        py_asink.thisown = True
        asink = dataiofactory.CreateDataIOSink(py_asink)
        # p2p_client.AddRemoteAudioSink("audio", asink)

        py_vsink = PythonVideoSink(DataIOType_I420)
        py_vsink.thisown = True
        vsink = dataiofactory.CreateDataIOSink(py_vsink)
        p2p_client.AddRemoteVideoSink("video", vsink)

        p2p_client.Login()
        return {"p2p_client" :p2p_client, "audio_sink":py_asink, "video_sink":py_vsink, "p2p_observer": p2p_observer}

def render(video_sink):
    cv2.namedWindow("YUV420p Renderer", cv2.WINDOW_NORMAL)
    while True:
        try:
            vframe = video_sink.vframe_queue.get(timeout = 1)
            cv2.imshow('YUV420p Renderer', vframe)
            print("render 1 frame")
            if cv2.waitKey(1) == ord('q'):
                break
            video_sink.vframe_queue.task_done()
        except Exception as e:
            pass
        finally:
            pass

def send_yuv(peer_data, yuv_file):
    yuv_file = open(yuv_file, "rb")
    width = int(1080)
    height = int(1920)
    y_vector = UINT8Vector()
    u_vector = UINT8Vector()
    v_vector = UINT8Vector()
    while True:
        y_vector.clear()
        u_vector.clear()
        v_vector.clear()
        y_byte = yuv_file.read(width * height)
        if not y_byte:
                yuv_file.seek(0)
                continue
        for i in range(width * height):
            y_vector.push_back(y_byte[i])

        u_byte = yuv_file.read(width * height // 4)
        if not u_byte:
            yuv_file.seek(0)
            continue
        for i in range(width * height // 4):
            u_vector.push_back(u_byte[i])

        v_byte = yuv_file.read(width * height // 4)
        if not v_byte:
            yuv_file.seek(0)
            continue
        for i in range(width * height // 4):
            v_vector.push_back(v_byte[i])
        
        # peer_data["video_source"].SetAdaption(False)
        peer_data["video_source"].OnDataYUVIn(width, height, y_vector, width, u_vector, width//2, v_vector, width//2)
        print("send yuv")
        time.sleep(0.001)
    yuv_file.close()

def send_pcm(peer_data, pcm_file):
    pcm_file = open(pcm_file, "rb")
    pcm_vector = UINT8Vector()
    while True:
        pcm_vector.clear()
        for i in range(240 * 2):
            pcm_byte = pcm_file.read(1)
            if not pcm_byte:
                pcm_file.seek(0)
                pcm_byte = pcm_file.read(1)
            pcm_vector.push_back(pcm_byte[0])

        peer_data["audio_source"].OnDataAudioIn(pcm_vector, 16, 24000, 1, 240)

        # print ('one time:',pcm_vector[0], pcm_vector.size())
        time.sleep(0.008)
    pcm_file.close()


def CreateSender():
    Controller.LoadConfigFile("./defaults.yaml")
    Controller.InitLog("./p2p_sender.log")

    time.sleep(3) # wait for receiver logined
    peer_data_1 = CreatePeer(is_sender=True, is_receiver=False)
    time.sleep(1)

    # assume the last id is of the sender
    receiver_id = last_id - 1
    print("ConnectToPeer (receiver_id = last_id - 1):", receiver_id)
    peer_data_1["p2p_client"].ConnectToPeer(receiver_id)

    send_yuv_thread = threading.Thread(target=send_yuv, args=(peer_data_1, "/path/to/video.yuv",))
    send_yuv_thread.start()

    send_pcm_thread = threading.Thread(target=send_pcm, args=(peer_data_1, "/path/to/video_24000_s16le.pcm",))
    send_pcm_thread.start()

    send_yuv_thread.join()
    send_pcm_thread.join()

def CreateReceiver():
    Controller.LoadConfigFile("./defaults.yaml")
    Controller.InitLog("./p2p_receiver.log")

    peer_data_2 = CreatePeer(is_sender=False, is_receiver=True)

    render(peer_data_2["video_sink"])

if __name__ == '__main__':
    send_yuv_process = multiprocessing.Process(target=CreateSender)
    send_yuv_process.start()

    send_pcm_process = multiprocessing.Process(target=CreateReceiver)
    send_pcm_process.start()

    # CreateReceiver()

    send_yuv_process.join()
    send_pcm_process.join()