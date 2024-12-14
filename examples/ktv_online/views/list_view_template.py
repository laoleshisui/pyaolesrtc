import json
import queue
from PyQt5.QtWidgets import QScrollArea, QLayoutItem, QGroupBox, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class UpdateListThread(QThread):
    add_item = pyqtSignal(object)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stop_flag = False
        self.q = queue.Queue()
    def __del__(self):
        print ("UpdateListThread __del__")

    def stop(self):
        print("UpdateListThread stop")
        self.stop_flag = True
        self.quit()
        self.wait()

    def run(self):
        while not self.stop_flag:
            try:
                data = self.q.get(timeout=0.1)
                self.add_item.emit(data)
            except queue.Empty:
                pass


class ListViewTemplate(QGroupBox):
    def __init__(self, config={}):
        super().__init__()
        self.title = config.get('title', None)
        self.list_button_label = config.get('list_button_label', "拉取列表")

        self.update_list_thread = UpdateListThread(self)
        self.update_list_thread.add_item.connect(self.add_item)
        self.update_list_thread.start()

        self.initUI()
    def __del__(self):
        print ("ListViewTemplate __del__")

    def stop(self):
        print("ListViewTemplate stop")
        self.update_list_thread.stop()

    #abstract method
    def view_from_itemdata(self, itemdata):
        pass

    def list_btn_clicked(self):
        pass

    def add_data(self, data):
        self.update_list_thread.q.put(data)

    def add_list_title(self, itemdata):
        itemview = self.view_from_itemdata(itemdata)
        if itemview != None:
            self.layout().insertWidget(1, itemview)
    def add_item(self, itemdata):
        itemview = self.view_from_itemdata(itemdata)
        if itemview != None:
            self.scroll_list_area.widget().layout().addWidget(itemview)
    def clear_items(self):
        layout = self.scroll_list_area.widget().layout()
        while layout.count():
            item = layout.takeAt(0)
            if item:
                widget = item.widget()
                layout.removeWidget(widget)
                widget.deleteLater()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        if self.title != None:
            self.setTitle(self.title)
        self.setFlat(False)
        self.setAlignment(Qt.AlignHCenter)
        self.layout().setAlignment(Qt.AlignTop)

        self.list_button = QPushButton(self.list_button_label, self)
        self.list_button.clicked.connect(self.list_btn_clicked)
        self.layout().addWidget(self.list_button, stretch=0)

        self.scroll_list_area = QScrollArea()
        scroll_list_content = QWidget()
        scroll_list_content.setLayout(QVBoxLayout())
        scroll_list_content.layout().setAlignment(Qt.AlignTop)
        self.scroll_list_area.setWidget(scroll_list_content)
        self.scroll_list_area.setWidgetResizable(True)
        self.layout().addWidget(self.scroll_list_area, stretch=1)