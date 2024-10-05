import sys
from collections import deque

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QTreeWidgetItem

import main_window_disigne

class FileManager(QWidget):
    def __init__(self, data):
        super(FileManager, self).__init__()
        self.ui = main_window_disigne.Ui_Form()
        self.ui.setupUi(self)

        self.headers = ['Sales', 'Marketing', 'HR']

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(self.headers)
        self.ui.tree.header().setDefaultSectionSize(180)
        #self.ui.tree.setModel(self.model)
        self.importData(data)
        self.ui.tree.expandAll()

    def importData(self, data):
        # addition data to the tree
        for parent in self.headers:
            parent_item = QTreeWidgetItem()
            parent_item.setText(0, parent)
            self.ui.tree.addTopLevelItem(parent_item)
            for child in data[parent]:
                child_item = QTreeWidgetItem()
                child_item.setText(0, child)
                parent_item.addChild(child_item)


if __name__ == '__main__':

    data = {
        'Sales': ['John', 'Jane', 'Peter'],
        'Marketing': ['Alice', 'Bob'],
        'HR': ['David']
    }

    app = QApplication(sys.argv)
    ex = FileManager(data)
    ex.show()
    app.exec_()