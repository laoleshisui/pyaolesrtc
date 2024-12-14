import json
import os
import threading
import time

import av
import weakref
from aolesrtc.aolesrtc import AudioBridgeClientObserver, Controller, DataIO, DataIOFactory, DataIOType_AUDIO, DataInput, DataOutput, JanusAudioBridgeClient, JanusCenterClient, JanusCenterObserver, ServiceDetail, UINT8Vector
from .sinks import FLVAudioSink


class KTVAudioBridgeObserver(AudioBridgeClientObserver):
    def __init__(self):
        super().__init__()
    def __del__(self):
        print ("KTVAudioBridgeObserver __del__")

    def setUI(self, ui):
        self.ui = weakref.ref(ui)

    def OnJsep(self, type, sdp):
        print('OnJsep:', type)
    def OnCreateRoom(self, handler_id, room_id):
        print('OnCreateRoom')
    def OnListRooms(self, handler_id, room_infos):
        print('OnListRooms', room_infos)
        if self.ui() is not None:
            self.ui().rooms_view.add_data(json.loads(room_infos))

    def OnListParticipants(self, handler_id, room_id, room_participants):
        print('OnListParticipants:', room_id, room_participants)
        if self.ui() is not None:
            self.ui().participants_view.add_data(json.loads(room_participants))

    def OnJoin(self, handler_id, room_id, id):
        print('OnJoin:', room_id, id)
    def OnLeave(self, handler_id, room_id, publisher_id):
        print('OnLeave')
    def OnDestroy(self, handler_id, room_id):
        print('OnDestroy')

class KTVAudioBridge():
    def __init__(self, janus_url='ws://101.133.238.239:8188', config_file='./defaults.yaml', log_file='./audiobridge.log'):
        Controller.LoadConfigFile(config_file)
        Controller.InitLog(log_file)
        self.stop_flag = False

        self.controller = Controller()
        self.audiobridge_client = JanusAudioBridgeClient(self.controller)
        self.ab_client_observer = KTVAudioBridgeObserver()

        self.audiobridge_client.AddObserver(self.ab_client_observer)

        self.audiobridge_client.CreateSession(janus_url)

        self.dataiofactory = DataIOFactory(self.controller)
    
    def __del__(self):
        print ("KTVAudioBridge __del__")

    def stop(self):
        print ("KTVAudioBridge stop")
        self.stop_flag = True

    def send_pcm_thread(self, audio_file_path, asource):
        print(os.path.splitext(audio_file_path)[1])
        if os.path.splitext(audio_file_path)[1] == '.pcm':
            self.send_pcm_file_thread(audio_file_path, asource)
        else:
            print('Demux file:', audio_file_path)
            container = av.open(audio_file_path)
            audio_stream = container.streams.audio[0]
            print("audio_stream.channels: ", audio_stream.channels)

            audio_resampler = av.audio.resampler.AudioResampler(format='s16', layout='mono', rate=24000)

            pcm_vector = UINT8Vector()
            for packet in container.demux(audio_stream):
                if self.stop_flag:
                    break
                for frame in packet.decode():
                    # print('frame.format.name:', frame.format.name)
                    # raw_audio_data = frame.to_ndarray().reshape(audio_stream.channels, -1)
                    # target_audio_data = raw_audio_data[0]
                    # if frame.format.name != 'pcm_s16le':
                    #     # assume the raw is float/double type
                    #     target_audio_data = (raw_audio_data[0] * np.iinfo(np.int16).max).astype(np.int16)

                    # pcm_bytes = target_audio_data.tobytes()

                    resampled_frames = audio_resampler.resample(frame)
                    for resampled_frame in resampled_frames:
                        pcm_bytes = resampled_frame.to_ndarray().tobytes()
                        pcm_bytes_len = len(pcm_bytes)

                        for i in range(pcm_bytes_len):
                            pcm_vector.push_back(pcm_bytes[i])

                            if not self.stop_flag and pcm_vector.size() == 240 * 2:
                                asource.OnDataAudioIn(pcm_vector, 16, 24000, 1, 240)
                                pcm_vector.clear()
                                time.sleep(0.008)

            container.close()


    def send_pcm_file_thread(self, pcm_file_path, asource):
        pcm_file = open(pcm_file_path, "rb")
        pcm_vector = UINT8Vector()
        while not self.stop_flag:
            pcm_vector.clear()
            for i in range(240 * 2):
                pcm_byte = pcm_file.read(1)
                if not pcm_byte:
                    pcm_file.seek(0)
                    pcm_byte = pcm_file.read(1)
                pcm_vector.push_back(pcm_byte[0])

            asource.OnDataAudioIn(pcm_vector, 16, 24000, 1, 240)

            time.sleep(0.008)
    def add_audio_source(self, pcm_file=None):
        asource = None
        if pcm_file == None:
            print('use microphone.')
        else:
            asource = self.dataiofactory.CreateDataIOSource(DataIOType_AUDIO)

            thread = threading.Thread(target=self.send_pcm_thread, args=(pcm_file, asource))
            thread.start()
        
        self.audiobridge_client.AddLocalAudioSource("audio", asource)

    def add_audio_sink(self, sink_file):
        self.py_asink = FLVAudioSink(DataIOType_AUDIO, sink_file)
        self.asink = self.dataiofactory.CreateDataIOSink(self.py_asink)
        self.audiobridge_client.AddRemoteAudioSink("janus", self.asink)

    def join(self, room_id, publisher_id, desc):
        #-5~256 error when cast
        if publisher_id >= -5 and publisher_id <= 256:
            return False
        self.audiobridge_client.Join(room_id, publisher_id, desc, '', False)
        time.sleep(1)
        self.audiobridge_client.ConfigureWithOffer()
        return True
