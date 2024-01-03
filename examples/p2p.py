import ctypes
import time

from aolesrtc.aolesrtc import Controller, DataIOFactory, DataIOType_AUDIO, DataIOType_I420, DataOutput, P2PClientDataIO, P2PModuleObserver, UINT8Vector

global last_id

class PythonAudioSink(DataOutput):
    def OnDataAudioOut(self, audio_data, bits_per_sample, sample_rate, number_of_channels, number_of_frames):
        print('OnDataAudioOut:', number_of_frames)
class PythonVideoSink(DataOutput):
    def OnDataYUVOut(self, id, width, height, data_y, stride_y, data_u, stride_u, data_v, stride_v):
        print('OnDataYUVOut:', width)

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
        asource = None # use microphone
        # p2p_client.AddLocalAudioSource("audio", asource)

        vsource = dataiofactory.CreateDataIOSource(DataIOType_I420)
        p2p_client.AddLocalVideoSource("video", vsource)

        p2p_client.Login()
        return {"p2p_client" :p2p_client, "audio_source":asource, "video_source":vsource, "p2p_observer": p2p_observer}
    if is_receiver:
        py_asink = PythonAudioSink(DataIOType_AUDIO)
        py_asink.thisown = False
        asink = dataiofactory.CreateDataIOSink(py_asink)
        # p2p_client.AddRemoteAudioSink("audio", asink)

        py_vsink = PythonVideoSink(DataIOType_I420)
        py_vsink.thisown = False
        vsink = dataiofactory.CreateDataIOSink(py_vsink)
        p2p_client.AddRemoteVideoSink("video", vsink)

        p2p_client.Login()
        return {"p2p_client" :p2p_client, "audio_sink":asink, "video_sink":vsink, "p2p_observer": p2p_observer}
    

if __name__ == '__main__':
    Controller.LoadConfigFile("./defaults.yaml")
    Controller.InitLog("./p2p.log")

    peer_data_1 = CreatePeer(is_sender=True, is_receiver=False)
    time.sleep(2)

    peer_data_2 = CreatePeer(is_sender=False, is_receiver=True)
    time.sleep(2)

    peer_data_1["p2p_client"].ConnectToPeer(last_id)
    # time.sleep(1000)

    yuv_file = open("/path/to/video.yuv", "rb")
    width = int(1080)
    height = int(1920)
    y_vector = UINT8Vector()
    u_vector = UINT8Vector()
    v_vector = UINT8Vector()
    while True:
        y_vector.clear()
        u_vector.clear()
        v_vector.clear()
        for i in range(width * height):
            y_byte = yuv_file.read(1)
            if not y_byte:
                yuv_file.seek(0)
                y_byte = yuv_file.read(1)
            y_vector.push_back(y_byte[0])
        for i in range(width * height // 4):
            u_byte = yuv_file.read(1)
            if not u_byte:
                yuv_file.seek(0)
                u_byte = yuv_file.read(1)
            u_vector.push_back(u_byte[0])
        for i in range(width * height // 4):
            v_byte = yuv_file.read(1)
            if not v_byte:
                yuv_file.seek(0)
                v_byte = yuv_file.read(1)
            v_vector.push_back(v_byte[0])
        peer_data_1["video_source"].SetAdaption(False)
        peer_data_1["video_source"].OnDataYUVIn(width, height, y_vector, width, u_vector, width//2, v_vector, width//2)
        time.sleep(0.020)

    pcm_file = open("/path/to/video_24000_s16le.pcm", "rb")
    pcm_vector = UINT8Vector()
    while True:
        pcm_vector.clear()
        for i in range(240 * 2):
            pcm_byte = pcm_file.read(1)
            if not pcm_byte:
                pcm_file.seek(0)
                pcm_byte = pcm_file.read(1)
            pcm_vector.push_back(pcm_byte[0])

        peer_data_1["audio_source"].OnDataAudioIn(pcm_vector, 16, 24000, 1, 240)

        # print ('one time:',pcm_vector[0], pcm_vector.size())
        time.sleep(0.008)
        

    pcm_file.close()