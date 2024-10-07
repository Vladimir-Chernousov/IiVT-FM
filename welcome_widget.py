import sys
from PyQt5 import QtCore, QtWidgets, QtGui


class NameClass(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        label = QtWidgets.QLabel()
        label.setText("Добро пожаловать!")
        label.setStyleSheet("""QLabel { color : #fff; 
                                       margin-top: 6px;
                                       margin-bottom: 6px;
                                       margin-left: 10px;
                                       margin-right: 10px; 
                                       font-size: 50px;}""")
        lay = QtWidgets.QVBoxLayout()
        lay.addWidget(label)

        self.setLayout(lay)
        self.adjustSize()
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity", self)
        self.animation.finished.connect(self.hide)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.hideAnimation)

    def paintEvent(self, event: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        rounded_rect = QtCore.QRect()
        rounded_rect.setX(self.rect().x() + 5)
        rounded_rect.setY(self.rect().y() + 5)
        rounded_rect.setWidth(self.rect().width() - 10)
        rounded_rect.setHeight(self.rect().height() - 10)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 0, 0, 180)))
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawRoundedRect(rounded_rect, 10, 10)

    def show(self):
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        pos = screen_geometry.center() - self.geometry().center()
        self.move(pos)
        self.setWindowOpacity(0.0)
        self.animation.setDuration(1500)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        super().show()
        self.animation.start()
        self.timer.start(3000)

    def hideAnimation(self):
        self.timer.stop()
        self.animation.setDuration(1500)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.start()

    def hide(self):
        if self.windowOpacity() == 0:
            super().hide()
            sys.exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = NameClass()
    w.show()
    sys.exit(app.exec_())
