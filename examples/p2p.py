import array
import queue
import ctypes
import threading
import time
import cv2
import numpy as np

from aolesrtc.aolesrtc import Controller, DataIOFactory, DataIOType_AUDIO, DataIOType_I420, DataOutput, P2PClientDataIO, P2PModuleObserver, UINT8Vector, cast_ptr_uint8_t, cast_ptr_void

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

    byte_array = array.array('B', [0]*(width*height * 3//2))
    address, arr_length = byte_array.buffer_info()
    y_byte_ptr = cast_ptr_uint8_t(address)
    u_byte_ptr = cast_ptr_uint8_t(address+width * height)
    v_byte_ptr = cast_ptr_uint8_t(address+width * height*5//4)
    while True:
        byte_read = yuv_file.readinto(byte_array)
        if byte_read < arr_length:
                yuv_file.seek(0)
                continue

        # peer_data["video_source"].SetAdaption(False)
        peer_data["video_source"].OnDataYUVIn(width, height, y_byte_ptr, width, u_byte_ptr, width//2, v_byte_ptr, width//2)

        print("send yuv")
        time.sleep(0.035)#  (1 / 25fps) - 5ms(used by runing code) = 35ms
    yuv_file.close()

def send_pcm(peer_data, pcm_file):
    pcm_file = open(pcm_file, "rb")

    byte_array = array.array('B', [0]*240 * 2)
    address, arr_length = byte_array.buffer_info()
    pcm_byte_ptr = cast_ptr_void(address)
    while True:
        byte_read = pcm_file.readinto(byte_array)
        if byte_read < arr_length:
            pcm_file.seek(0)
            continue

        peer_data["audio_source"].OnDataAudioIn(pcm_byte_ptr, 16, 24000, 1, 240)
        time.sleep(0.008)
    pcm_file.close()


if __name__ == '__main__':
    Controller.LoadConfigFile("./defaults.yaml")
    Controller.InitLog("./p2p.log")

    peer_data_1 = CreatePeer(is_sender=True, is_receiver=False)
    time.sleep(2)

    peer_data_2 = CreatePeer(is_sender=False, is_receiver=True)
    time.sleep(2)

    peer_data_1["p2p_client"].ConnectToPeer(last_id)

    send_yuv_thread = threading.Thread(target=send_yuv, args=(peer_data_1, "/path/to/metaman-synthetise/video.yuv",))
    send_yuv_thread.start()

    send_pcm_thread = threading.Thread(target=send_pcm, args=(peer_data_1, "/path/to/video_24000_s16le.pcm",))
    send_pcm_thread.start()

    render(peer_data_2["video_sink"])

    send_yuv_thread.join()
    send_pcm_thread.join()