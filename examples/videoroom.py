import ctypes
import time

from aolesrtc.aolesrtc import Controller, DataIO, DataIOFactory, DataIOType_AUDIO, DataInput, DataOutput, JanusCenterClient, JanusCenterObserver, JanusVideoRoomClientDataIO, ServiceDetail, UINT8Vector, VideoRoomClientObserver

global janus_url
janus_url = 'ws://101.133.238.239:8188'

class PythonAudioSink(DataOutput):
    def OnDataAudioOut(self, audio_data, bits_per_sample, sample_rate, number_of_channels, number_of_frames):
        print('OnDataAudioOut:', number_of_frames)

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

class JanusClientObserver(VideoRoomClientObserver):
    vr = None

    def __init__(self, vr):
        super().__init__()
        self.vr = vr

    def OnJsep(self, type, sdp):
        print('OnJsep:', type)
    def OnCreateRoom(self, handler_id, room_id):
        print('OnCreateRoom')
    def OnListRooms(self, handler_id, room_infos):
        print('OnListRooms')
    def OnListParticipants(self, handler_id, room_id, room_participants):
        print('OnListParticipants:', room_id, room_participants)
        self.vr.Subscribe(1234, [1234])
    def OnJoinAsPublisher(self, handler_id, room_id, publisher_id):
        print('OnJoinAsPublisher:', handler_id, room_id, publisher_id)
    def OnJoinAsSubscriber(self, handler_id, room_id):
        print('OnJoinAsSubscriber')
    def OnLeave(self, handler_id, room_id, publisher_id):
        print('OnLeave')

if __name__ == '__main__':
    Controller.LoadConfigFile("./defaults.yaml")
    Controller.InitLog("./videoroom.log")
    controller = Controller()

    # janus_center_client = JanusCenterClient(controller)
    # janus_center_observer = JanusCenterClientObserver()
    # janus_center_client.AddObserver(janus_center_observer)
    # janus_center_client.GetJanus()
    # time.sleep(2)

    videoroom_client = JanusVideoRoomClientDataIO(controller)
    vr_client_observer = JanusClientObserver(videoroom_client)

    videoroom_client.AddVideoRoomClientObserver(vr_client_observer)

    print("janus_url:", janus_url)
    videoroom_client.CreateSession(janus_url)
    time.sleep(0.1)

    dataiofactory = DataIOFactory(controller)
    asource = dataiofactory.CreateDataIOSource(DataIOType_AUDIO)

    py_asink = PythonAudioSink(DataIOType_AUDIO)
    py_asink.thisown = True
    asink = dataiofactory.CreateDataIOSink(py_asink)

    videoroom_client.AddLocalAudioSource("audio", asource)
    # videoroom_client.AddLocalAudioSink("audio", asink)
    videoroom_client.AddRemoteAudioSink("janus", asink)
    videoroom_client.Publish(1234, 1234, "aoles") #-5~256 error when cast
    time.sleep(1)

    videoroom_client.ListParticipants(1234)

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

        # print ('one time:',pcm_vector[0], pcm_vector.size())
        time.sleep(0.008)
        

    pcm_file.close()