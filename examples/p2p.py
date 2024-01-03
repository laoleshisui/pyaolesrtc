import ctypes
import time

from aolesrtc.aolesrtc import Controller, DataIOFactory, DataIOType_AUDIO, DataOutput, P2PClientDataIO, P2PModuleObserver, UINT8Vector

global last_id

class PythonAudioSink(DataOutput):
    def OnDataAudioOut(self, audio_data, bits_per_sample, sample_rate, number_of_channels, number_of_frames):
        print('OnDataAudioOut:', number_of_frames)

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
        source = dataiofactory.CreateDataIOSource(DataIOType_AUDIO)
        source = None
        p2p_client.AddLocalAudioSource("audio", source)
        p2p_client.Login()
        return {"p2p_client" :p2p_client, "audio_source":source, "p2p_observer": p2p_observer}
    if is_receiver:
        py_asink = PythonAudioSink(DataIOType_AUDIO)
        sink = dataiofactory.CreateDataIOSink(py_asink)
        p2p_client.AddLocalAudioSink("audio", sink)
        p2p_client.Login()
        return {"p2p_client" :p2p_client, "audio_sink":sink, "p2p_observer": p2p_observer}
    

if __name__ == '__main__':
    Controller.LoadConfigFile("./defaults.yaml")
    Controller.InitLog("./p2p.log")

    peer_data_1 = CreatePeer(is_sender=True, is_receiver=False)
    time.sleep(2)

    peer_data_2 = CreatePeer(is_sender=False, is_receiver=True)
    time.sleep(2)

    peer_data_1["p2p_client"].ConnectToPeer(last_id)
    time.sleep(1000)

    # pcm_file = open("/path/to/video_24000_s16le.pcm", "rb")
    # pcm_vector = UINT8Vector()
    # while True:
    #     pcm_vector.clear()
    #     for i in range(240 * 2):
    #         pcm_byte = pcm_file.read(1)
    #         if not pcm_byte:
    #             pcm_file.seek(0)
    #             pcm_byte = pcm_file.read(1)
    #         pcm_vector.push_back(pcm_byte[0])

    #     peer_data_1["audio_source"].OnDataAudioIn(pcm_vector, 16, 24000, 1, 240)

    #     # print ('one time:',pcm_vector[0], pcm_vector.size())
    #     time.sleep(0.008)
        

    # pcm_file.close()