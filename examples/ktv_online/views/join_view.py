import datetime
import os
import weakref
from PyQt5.QtWidgets import QGroupBox, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class JoinView(QGroupBox):
    def __init__(self, ab):
        super().__init__()

        self.ab = weakref.ref(ab)

        self.initUI()
    def __del__(self):
        print ("JoinView __del__")

    def join_btn_clicked(self):
        pcm_file = self.pcm_source_edit.text()
        print('pcm source: ', pcm_file)
        if len(pcm_file) == 0 or not os.path.isfile(pcm_file):
            print('pcm source is invalid!')
            if self.ab() is not None:
                self.ab().add_audio_source()
        else:
            if self.ab() is not None:
                self.ab().add_audio_source(pcm_file)

        sink_file = self.sink_edit.text()
        print("add_audio_sink:", sink_file)
        if len(sink_file) != 0 and  self.ab() is not None:
            self.ab().add_audio_sink(sink_file)
        if self.ab() is not None:
            self.ab().join(int(self.room_id_edit.text()), int(self.pulisher_id_edit.text()), self.desc_edit.text())


    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setFlat(False)
        self.setAlignment(Qt.AlignHCenter)
        self.layout().setAlignment(Qt.AlignTop)

        self.room_id_edit = QLineEdit(self)
        self.room_id_edit.setPlaceholderText('房间号')
        self.layout().addWidget(self.room_id_edit)

        self.pulisher_id_edit = QLineEdit(self)
        self.pulisher_id_edit.setPlaceholderText('发布号')
        self.layout().addWidget(self.pulisher_id_edit)

        self.desc_edit = QLineEdit(self)
        self.desc_edit.setPlaceholderText('发布者描述')
        self.layout().addWidget(self.desc_edit)

        self.pcm_source_edit = QLineEdit(self)
        self.pcm_source_edit.setPlaceholderText('音频源')
        self.layout().addWidget(self.pcm_source_edit)

        self.sink_edit = QLineEdit(self)
        self.sink_edit.setPlaceholderText('录制文件路径')
        time_format = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        auto_file_path = os.path.join(os.path.expanduser("~")+'/Downloads/', f"recode_{time_format}.flv")
        self.sink_edit.setText(auto_file_path)
        self.layout().addWidget(self.sink_edit)

        self.join_button = QPushButton('加入', self)
        self.join_button.clicked.connect(self.join_btn_clicked)
        self.layout().addWidget(self.join_button)
