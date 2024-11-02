import sys
from collections import deque
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QMainWindow, QMenu

import main_window_disigne

class FileManager(QMainWindow):
    def __init__(self):
        super(FileManager, self).__init__()
        self.ui = main_window_disigne.Ui_MainWindow()
        self.ui.setupUi(self)

        path = QDir.rootPath()

        self.model = QFileSystemModel()
        self.model.setRootPath(path)

        self.ui.tree.setModel(self.model)
        self.ui.tree.setSelectionMode(QTreeView.ExtendedSelection)

        self.ui.pbn_cut.clicked.connect(self.pbn_cut)
        self.ui.pbn_copy.clicked.connect(self.pbn_copy)
        self.ui.pbn_paste.clicked.connect(self.pbn_paste)
        self.ui.pbn_delete.clicked.connect(self.pbn_delete)
        self.ui.pbn_info.clicked.connect(self.pbn_info)

        self.ui.actioninfo.triggered.connect(self.menu_info)


    def pbn_cut(self):
        pass

    def pbn_copy(self):
        pass

    def pbn_paste(self):
        pass

    def pbn_delete(self):
        pass

    def pbn_info(self):
        pass

    def menu_info(self):
        pass

    '''def contextMenuEvent(self, event):
        contextMenu = QMenu()

        newAction = contextMenu.addAction("New")

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quit:
            self.close()'''


def main():
    app = QApplication(sys.argv)
    ex = FileManager()
    ex.show()
    app.exec_()