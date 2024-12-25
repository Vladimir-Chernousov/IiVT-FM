import sys
import os
from collections import deque
from PyQt5.QtCore import QDir, QModelIndex
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

        self.ui.actioninfo.triggered.connect(self.pbn_info)
        self.ui.actioncopy_2.triggered.connect(self.pbn_copy)
        self.ui.actioncut.triggered.connect(self.pbn_cut)
        self.ui.actionpaste.triggered.connect(self.pbn_paste)
        self.ui.actiondelete.triggered.connect(self.pbn_delete)
        self.ui.actionAbout_FileManager.triggered.connect(self.about)

    currentPath = ''
    commandString = ''
    isDirectory = True
    def on_tree_clicked(self, index):
        self.currentPath = self.model.filePath(index).replace('/', '\\')
        self.isDirectory = self.model.isDir(index)



    def pbn_cut(self):
        print('cut')
        self.commandString = 'move /y "' + self.currentPath + '"'

    def pbn_copy(self):
        print('copy')
        self.commandString = 'xcopy /e /s /y "' + self.currentPath + '"'
        print(self.commandString)

    def pbn_paste(self):
        print('paste')
        if (self.commandString != ''):
            try:
                if (self.isDirectory):
                    self.commandString += ' "' + self.currentPath + '"'
                else:
                    self.commandString += ' "' + '\\'.join(self.currentPath.split('\\')[:-1]) + '"'
                print(self.commandString)
                os.system(self.commandString)
                self.commandString = ''
            except:
                pass

    def pbn_delete(self):
        print('delete')
        print('del /s /y "' + self.currentPath + '"')
        try:
            os.system('del "' + self.currentPath + '"')
        except:
            pass

    def pbn_info(self):
        print('pbn_info')

    def about(self):
        print('about')

    def contextMenuEvent(self, event):
        contextMenu = QMenu()

        copyAction = contextMenu.addAction("copy")
        cutAction = contextMenu.addAction("cut")
        pasteAction = contextMenu.addAction("paste")
        deleteAction = contextMenu.addAction("delete")

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quit:
            self.close()
        elif action == copyAction:
            self.pbn_copy()
        elif action == cutAction:
            self.pbn_cut()
        elif action == pasteAction:
            self.pbn_paste()
        elif action == deleteAction:
            self.pbn_delete()

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == 67 or event.key() == 16777268:
            self.pbn_copy()
        elif event.key() == 86:
            self.pbn_paste()
        elif event.key() == 88:
            self.pbn_cut()
        elif event.key() == 16777272 or event.key() == 81:
            self.pbn_delete()
        elif event.key() == 16777264:
            self.about()
        event.accept()



def main():
    os.system("chcp 65001 > nul")
    app = QApplication(sys.argv)
    ex = FileManager()
    ex.show()
    app.exec_()