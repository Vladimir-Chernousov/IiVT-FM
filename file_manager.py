import sys
import os
import webbrowser
from collections import deque
from operator import index

import requests
from PyQt5.QtCore import QDir, QFileInfo
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QMainWindow, QMenu, QMessageBox, QHeaderView
from PyQt5.uic.Compiler.qtproxies import QtWidgets
from urllib3 import HTTPConnectionPool

import main_window_disigne

class FileManager(QMainWindow):
    def __init__(self):
        super(FileManager, self).__init__()
        self.ui = main_window_disigne.Ui_MainWindow()
        self.ui.setupUi(self)

        self.path = QDir.rootPath()

        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)
        self.model.setFilter(QDir.NoFilter)  # Скрытые и системные файлы

        self.ui.tree.setModel(self.model)
        self.ui.tree.setSelectionMode(QTreeView.ExtendedSelection)
        self.ui.tree.header().setSectionResizeMode(0, QHeaderView.Stretch)

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
        self.ui.actionPaint.triggered.connect(self.open_paint)
        self.ui.actionCalk.triggered.connect(self.open_calc)
        self.ui.actionBlok.triggered.connect(self.open_notepad)
        self.ui.actionDispetcher.triggered.connect(self.open_taskmgr)
        self.ui.actionCmd.triggered.connect(self.open_cmd)
        self.ui.actionParametrs.triggered.connect(self.open_parameters)
        self.ui.actionRedgedit.triggered.connect(self.open_redgedit)

        self.ui.checkBox.clicked.connect(self.choose_box)

        self.current_path = ''
        self.command_string = ''
        self.is_dir = True

    def on_tree_clicked(self, index):
        self.current_path = self.model.filePath(index).replace('/', '\\')
        self.is_dir = self.model.isDir(index)

    def choose_box(self):
        if self.ui.checkBox.isChecked():
            self.model.setFilter(QDir.NoFilter)
        else:
            self.model.setFilter(QDir.AllDirs | QDir.Files)

    def pbn_cut(self):
        if self.current_path == '':
            QMessageBox.about(self, 'Оповещение', 'Ничего не выбрано')
            return None
        self.command_string = 'move /y "' + self.current_path + '"'

    def pbn_copy(self):
        if self.current_path == '':
            QMessageBox.about(self, 'Оповещение', 'Ничего не выбрано')
            return None
        if self.is_dir:
            self.command_string = 'xcopy /e /s /y "' + self.current_path + '"'
        else:
            self.command_string = 'copy /y "' + self.current_path + '"'

    def pbn_paste(self):
        if self.command_string != '':
            try:
                if self.is_dir:
                    self.command_string += ' "' + self.current_path + '"'
                else:
                    self.command_string += ' "' + '\\'.join(self.current_path.split('\\')[:-1]) + '"'
                print(self.command_string)
                os.system(self.command_string)
                self.command_string = ''
            except Exception as e:
                QMessageBox.about(self, 'Оповещение', e.__str__())
        else:
            QMessageBox.about(self, 'Оповещение', 'Ничего не выбрано')
            return None

    def pbn_delete(self):
        if self.current_path == '':
            QMessageBox.about(self, 'Оповещение', 'Ничего не выбрано')
            return None
        try:
            os.system('del "' + self.current_path + '"')
        except Exception as e:
            QMessageBox.about(self, 'Оповещение', e.__str__())

    def pbn_info(self):
        full_path = "Полный путь к файлу: " + self.current_path + "\n"
        last_open = "Последнее открытие: " + QFileInfo(self.current_path).lastRead().toString("dd-MM-yyyy HH:mm:ss") + "\n"
        max_len = max(len(full_path), len(last_open))
        if max_len == len(full_path):
            sub = len(full_path) - len(last_open)
            last_open = "Последнее открытие: " + sub * " " + QFileInfo(self.current_path).lastRead().toString("dd-MM-yyyy HH:mm:ss") + "\n"
        else:
            sub = len(last_open) - len(full_path)
            full_path = "Полный путь к файлу: " + sub * " " + self.current_path + "\n"

        len_file_size = len("Размер файла :" + f"{QFileInfo(self.current_path).size() / 1024:.3f} kByte" + "\n")
        file_size = "Размер файла :" + (max_len - len_file_size) * " " + f"{QFileInfo(self.current_path).size() / 1024:.3f} kByte" + "\n"
        len_suffix = len(str(QFileInfo(self.current_path).suffix())) + 12
        if QFileInfo(self.current_path).isExecutable():
            is_ex = "Да"
            len_ex = 16
        else:
            is_ex = "Нет"
            len_ex = 17

        if QFileInfo(self.current_path).isHidden():
            is_hide = "Да"
            len_hide = 12
        else:
            is_hide = "Нет"
            len_hide = 13

        if not QFileInfo(self.current_path).isWritable():
            is_not_read = "Да"
            len_not_read = 22
        else:
            is_not_read = "Нет"
            len_not_read = 23

        if self.current_path != '':
            msg_text = "Создание: " + (max_len - 30) * " " + QFileInfo(self.current_path).created().toString("dd-MM-yyyy HH:mm:ss") + "\n"
            msg_text += "Изменение: " + (max_len - 31) * " " + QFileInfo(self.current_path).lastModified().toString("dd-MM-yyyy HH:mm:ss") + "\n"
            msg_text += last_open
            msg_text += file_size
            msg_text += full_path
            if self.is_dir:
                msg_text += "Тип файла: " + (max_len - 15) * " " + "dir\n"
            else:
                msg_text += "Тип файла: " + (max_len - len_suffix) * " " + QFileInfo(self.current_path).suffix() + "\n"
            msg_text += "Исполняемый: " + (max_len - len_ex) * " " + is_ex + "\n"
            msg_text += "Скрытый: " + (max_len - len_hide) * " " + is_hide + "\n"
            msg_text += "Только для чтения: " + (max_len - len_not_read) * " " + is_not_read
        else:
            msg_text = "Файл не выбран."
        msg = QMessageBox()
        msg.setWindowTitle("Информация о файле")
        msg.setText(msg_text)
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet(
            """
            QMessageBox {
                font-family: consolas;
            }         
            """
        )
        msg.exec_()

    def about(self):
        try:
            requests.get("http://193.124.22.221")
            os.system("start http://193.124.22.221/")
        except Exception:
            webbrowser.open("about.html")

    def new_folder(self):
        if self.is_dir:
            try:
                os.system('mkdir "' + self.current_path + '\\' + 'Hello' + '"')
            except:
                QMessageBox.about(self, 'Оповещение', e.__str__())
        else:
            try:
                os.system('mkdir "' + '\\'.join(self.current_path.split('\\')[:-1]) + '\\' + 'Hello' + '"')
            except:
                QMessageBox.about(self, 'Оповещение', e.__str__())


    def rename(self):
        try:
            os.system('rename "' + self.current_path +'" Hello.txt')
        except:
            QMessageBox.about(self, 'Оповещение', e.__str__())


    def open(self):
        if self.current_path != '':
            print ('start "' + self.current_path + '"')
            os.system('start notepad "' + self.current_path + '"')

    def open_paint(self):
        os.system("start mspaint")

    def open_calc(self):
        os.system("start calc")

    def open_notepad(self):
        os.system("start notepad")

    def open_taskmgr(self):
        os.system("start taskmgr")

    def open_cmd(self):
        os.system("start cmd")

    def open_parameters(self):
        os.system("start msconfig")

    def open_redgedit(self):
        os.system("start regedit")

    def contextMenuEvent(self, event):
        contextMenu = QMenu()

        copyAction = contextMenu.addAction("copy")
        cutAction = contextMenu.addAction("cut")
        pasteAction = contextMenu.addAction("paste")
        deleteAction = contextMenu.addAction("delete")
        newAction = contextMenu.addAction("New folder")
        renameAction = contextMenu.addAction("Rename")
        openAction = contextMenu.addAction("Open as text")

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
        elif action == newAction:
            self.new_folder()
        elif action == renameAction:
            self.rename()
        elif action == openAction:
            self.open()

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == 67 or event.key() == 16777268:
            self.pbn_copy()
        elif event.key() == 86:
            self.pbn_paste()
        elif event.key() == 88:
            self.pbn_cut()
        elif event.key() == 16777272 or event.key() == 16777223 or event.key() == 81:
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