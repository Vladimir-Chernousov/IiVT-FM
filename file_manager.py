import sys
from collections import deque
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QMainWindow

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


def main():
    app = QApplication(sys.argv)
    ex = FileManager()
    ex.show()
    app.exec_()