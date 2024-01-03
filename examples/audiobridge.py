import ctypes
import time

from aolesrtc.aolesrtc import AudioBridgeClientObserver, Controller, DataIO, DataIOFactory, DataIOType_AUDIO, DataInput, DataOutput, JanusAudioBridgeClient, JanusCenterClient, JanusCenterObserver, ServiceDetail, UINT8Vector

global janus_url
janus_url = 'ws://101.133.238.239:8188'

class PythonAudioSink(DataOutput):
    def OnDataAudioOut(self, audio_data, bits_per_sample, sample_rate, number_of_channels, number_of_frames):
        print('OnDataAudioOut:', number_of_frames)
        pass

class JanusCenterClientObserver(JanusCenterObserver):
    def OnGetJanus(self, *args):
        if len(args) > 0:
            arg = args[0]
            if isinstance(arg, ServiceDetail):
                name_value = arg.name
                description_value = arg.description
                ip_value = arg.ip
                port_value = arg.port
                
                global janus_url
                janus_url = f'ws://{ip_value}:{port_value}'

                print('OnGetJanus', name_value, description_value, ip_value, port_value)

class JanusClientObserver(AudioBridgeClientObserver):
    ab = None

    def __init__(self, ab):
        super().__init__()
        self.ab = ab

    def OnJsep(self, type, sdp):
        print('OnJsep:', type)
    def OnCreateRoom(self, handler_id, room_id):
        print('OnCreateRoom')
    def OnListRooms(self, handler_id, room_infos):
        print('OnListRooms')
    def OnListParticipants(self, handler_id, room_id, room_participants):
        print('OnListParticipants:', room_id, room_participants)
    def OnJoin(self, handler_id, room_id, id):
        print('OnJoin:', room_id, id)
    def OnLeave(self, handler_id, room_id, publisher_id):
        print('OnLeave')
    def OnDestroy(self, handler_id, room_id):
        print('OnDestroy')

if __name__ == '__main__':
    Controller.LoadConfigFile("./defaults.yaml")
    Controller.InitLog("./audiobridge.log")
    controller = Controller()

    janus_center_client = JanusCenterClient(controller)
    janus_center_observer = JanusCenterClientObserver()
    janus_center_client.AddObserver(janus_center_observer)
    janus_center_client.GetJanus()
    time.sleep(2)

    audiobridge_client = JanusAudioBridgeClient(controller)
    ab_client_observer = JanusClientObserver(audiobridge_client)

    audiobridge_client.AddObserver(ab_client_observer)

    audiobridge_client.CreateSession(janus_url)
    time.sleep(2)

    dataiofactory = DataIOFactory(controller)
    asource = dataiofactory.CreateDataIOSource(DataIOType_AUDIO)
    py_asink = PythonAudioSink(DataIOType_AUDIO)
    asink = dataiofactory.CreateDataIOSink(py_asink)

    audiobridge_client.AddLocalAudioSource("audio", asource)
    audiobridge_client.AddLocalAudioSink("audio", asink)
    audiobridge_client.Join(1234, 1234, "aoles", '', False) #-5~256 error when cast
    time.sleep(10)
    audiobridge_client.ConfigureWithOffer()

    audiobridge_client.ListParticipants(1234)

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

        asource.OnDataAudioIn(pcm_vector, 16, 24000, 1, 240)

        time.sleep(0.008)
        

    pcm_file.close()