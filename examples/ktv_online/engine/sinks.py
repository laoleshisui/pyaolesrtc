import av
import numpy as np
from aolesrtc.aolesrtc import DataOutput
from .utils import GetData


class FLVAudioSink(DataOutput):
    def __init__(self, type, sink_file):
        super().__init__(type)
        self.output = av.open(sink_file, 'w', 'flv')

        self.audio_stream = self.output.add_stream('aac')
        # self.audio_stream.bit_rate = 192000
        self.audio_stream.channels = 1
        self.audio_stream.format = 'fltp'
    def __del__(self):
        for packet in self.audio_stream.encode(None):
            self.output.mux(packet)
        self.output.close()

    def OnDataAudioOut(self, audio_data, bits_per_sample, sample_rate, number_of_channels, number_of_frames):
        # print('OnDataAudioOut:', bits_per_sample, sample_rate, number_of_channels, number_of_frames)

        py_audio_data_bytes = GetData(audio_data, int(number_of_frames*bits_per_sample/8))
        frame = av.AudioFrame.from_ndarray(
            np.frombuffer(py_audio_data_bytes, dtype=np.int16).reshape(1, -1).astype(np.float32)/np.iinfo(np.int16).max,
            format='fltp',
            layout='mono',
        )
        frame.sample_rate = sample_rate
        # self.audio_stream.sample_rate = sample_rate
        for packet in self.audio_stream.encode(frame):
            self.output.mux(packet)