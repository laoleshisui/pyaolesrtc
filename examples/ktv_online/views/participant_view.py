import json
import queue
import weakref
from PyQt5.QtWidgets import QGroupBox, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

from views.list_view_template import ListViewTemplate

class ParticipantListItem(QWidget):
    def __init__(self, itemdata, parent=None):
        super(ParticipantListItem, self).__init__(parent)
        
        layout = QHBoxLayout()
        layout.addWidget(QLabel(str(itemdata.get('display', None))), stretch=2)
        layout.addWidget(QLabel(str(itemdata.get('id', None))), stretch=1)
        layout.addWidget(QLabel(str(itemdata.get('muted', None))), stretch=1)
        layout.addWidget(QLabel(str(itemdata.get('setup', None))), stretch=1)
        layout.addWidget(QLabel(str(itemdata.get('talking', None))), stretch=1)
        
        self.setLayout(layout)

class ParticipantView(ListViewTemplate):
    def __init__(self, ab, room_id_edit):
        super().__init__(config={"list_button_label":"拉取成员列表"})

        self.ab = weakref.ref(ab)
        self.room_id_edit = room_id_edit

        title_config = {
            "display" : "描述",
            "id" : "ID",
            "muted" : "静音",
            "setup" : "连接",
            "talking" : "说话中"
        }
        self.add_list_title(title_config)

    def add_data(self, data):
        for item in data:
            item['participant_view_task'] = True
            super().add_data(data=item)

    def view_from_itemdata(self, itemdata):
        if itemdata.get('participant_view_task', True):
            return ParticipantListItem(itemdata)
        else:
            return None

    def list_btn_clicked(self):
        self.clear_items()
        room_id = int(self.room_id_edit.text())
        if self.ab() is not None:
            self.ab().audiobridge_client.ListParticipants(room_id)