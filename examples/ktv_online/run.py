import sys
import threading
import time
import av
from PyQt5.QtWidgets import QGroupBox, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
import numpy as np

from engine.ktv_audiobridge import KTVAudioBridge
from views.room_view import RoomView
from views.participant_view import ParticipantView
from views.join_view import JoinView

class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.ab = KTVAudioBridge()
        self.initUI()

        self.ab.ab_client_observer.setUI(self)

    def __del__(self):
        print("UI __del__")
        self.ab.stop()
        self.rooms_view.stop()
        self.participants_view.stop()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setGeometry(100, 100, 400, 1000)

        self.join_view = JoinView(self.ab)
        self.layout().addWidget(self.join_view, stretch=0)

        self.rooms_view = RoomView(self.ab)
        self.layout().addWidget(self.rooms_view, stretch=1)

        self.participants_view = ParticipantView(self.ab, self.join_view.room_id_edit)
        self.layout().addWidget(self.participants_view, stretch=1)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    app.exec_()
    del ui