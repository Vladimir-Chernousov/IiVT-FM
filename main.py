import sys
from collections import deque

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QFileSystemModel, QTreeView

import main_window_disigne

class FileManager(QWidget):
    def __init__(self, data):
        super(FileManager, self).__init__()
        self.ui = main_window_disigne.Ui_Form()
        self.ui.setupUi(self)

        path = QDir.rootPath()

        self.model = QFileSystemModel()
        self.model.setRootPath(path)

        self.ui.tree.setModel(self.model)
        self.ui.tree.setSelectionMode(QTreeView.ExtendedSelection)

        #self.headers = ['Name', 'Height', 'Weight']

        #self.model = QStandardItemModel(self)
        #self.model.setHorizontalHeaderLabels(self.headers)

        #self.ui.tree.header().setDefaultSectionSize(180)
        #self.ui.tree.setModel(self.model)
        #self.importData(data)
        #self.ui.tree.expandAll()

    def importData(self, data, root=None):
        self.model.setRowCount(0)
        if root is None:
            root = self.model.invisibleRootItem()
        seen = {}   # List of  QStandardItem
        values = deque(data)
        while values:
            value = values.popleft()
            if value['unique_id'] == 1:
                parent = root
            else:
                pid = value['parent_id']
                if pid not in seen:
                    values.append(value)
                    continue
                parent = seen[pid]
            unique_id = value['unique_id']
            parent.appendRow([
                QStandardItem(value['short_name']),
                QStandardItem(value['height']),
                QStandardItem(value['weight'])
            ])
            seen[unique_id] = parent.child(parent.rowCount() - 1)


if __name__ == '__main__':
    data = [
        {'unique_id': 1, 'parent_id': 0, 'short_name': '', 'height': ' ', 'weight': ' '},
        {'unique_id': 2, 'parent_id': 1, 'short_name': 'Class 1', 'height': ' ', 'weight': ' '},
        {'unique_id': 3, 'parent_id': 2, 'short_name': 'Lucy', 'height': '162', 'weight': '50'},
        {'unique_id': 4, 'parent_id': 2, 'short_name': 'Joe', 'height': '175', 'weight': '65'},
        {'unique_id': 5, 'parent_id': 1, 'short_name': 'Class 2', 'height': ' ', 'weight': ' '},
        {'unique_id': 6, 'parent_id': 5, 'short_name': 'Lily', 'height': '170', 'weight': '55'},
        {'unique_id': 7, 'parent_id': 5, 'short_name': 'Tom', 'height': '180', 'weight': '75'},
        {'unique_id': 8, 'parent_id': 1, 'short_name': 'Class 3', 'height': ' ', 'weight': ' '},
        {'unique_id': 9, 'parent_id': 8, 'short_name': 'Jack', 'height': '178', 'weight': '80'},
        {'unique_id': 10, 'parent_id': 8, 'short_name': 'Tim', 'height': '172', 'weight': '60'},
        {'unique_id': 11, 'parent_id': 12, 'short_name': 'Vova', 'height': '172', 'weight': '100'},
        {'unique_id': 12, 'parent_id': 2, 'short_name': 'Serjey', 'height': '172', 'weight': '60'}

    ]

    app = QApplication(sys.argv)
    ex = FileManager(data)
    ex.show()
    app.exec_()