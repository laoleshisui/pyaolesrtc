import json
import queue
import weakref
from PyQt5.QtWidgets import QGroupBox, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

from views.list_view_template import ListViewTemplate

class RoomListItem(QWidget):
    def __init__(self, itemdata, parent=None):
        super(RoomListItem, self).__init__(parent)

        layout = QHBoxLayout()
        layout.addWidget(QLabel(str(itemdata.get('description', None))), stretch=2)
        layout.addWidget(QLabel(str(itemdata.get('room', None))), stretch=1)
        layout.addWidget(QLabel(str(itemdata.get('muted', None))), stretch=1)
        layout.addWidget(QLabel(str(itemdata.get('num_participants', None))), stretch=1)
        layout.addWidget(QLabel(str(itemdata.get('pin_required', None))), stretch=1)
        
        self.setLayout(layout)

class RoomView(ListViewTemplate):
    def __init__(self, ab):
        super().__init__(config={"list_button_label":"拉取房间列表"})

        self.ab = weakref.ref(ab)

        title_config = {
            "description" : "描述",
            "muted" : "静音",
            "num_participants" : "人数",
            "pin_required" : "密码",
            "room" : "房号"
        }
        self.add_list_title(title_config)

    def add_data(self, data):
        for item in data:
            item['room_view_task'] = True
            super().add_data(data=item)

    def view_from_itemdata(self, itemdata):
        if itemdata.get('room_view_task', True):
            return RoomListItem(itemdata)
        else:
            return None

    def list_btn_clicked(self):
        self.clear_items()
        if self.ab() is not None:
            self.ab().audiobridge_client.ListRooms()