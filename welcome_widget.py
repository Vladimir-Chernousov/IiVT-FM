import sys

from PyQt5.QtCore import QPropertyAnimation, QTimer, Qt, QRect
from PyQt5.QtGui import QColor, QBrush, QPaintEvent, QPainter
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QDialog


class Welcome(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        label = QLabel()
        label.setText("ЛУЧШИЙ ФАЙЛОВЫЙ МЕНЕНДЖЕР НА ПЛАНЕТЕ ЗЕМЛЯ!")
        label.setStyleSheet("""QLabel { color : #fff; 
                                       margin-top: 6px;
                                       margin-bottom: 6px;
                                       margin-left: 10px;
                                       margin-right: 10px; 
                                       font-size: 50px;}""")
        lay = QVBoxLayout()
        lay.addWidget(label)

        self.setLayout(lay)
        self.adjustSize()
        self.animation = QPropertyAnimation(self, b"windowOpacity", self)
        self.animation.finished.connect(self.hide)
        self.timer = QTimer()
        self.timer.timeout.connect(self.hideAnimation)

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rounded_rect = QRect()
        rounded_rect.setX(self.rect().x() + 5)
        rounded_rect.setY(self.rect().y() + 5)
        rounded_rect.setWidth(self.rect().width() - 10)
        rounded_rect.setHeight(self.rect().height() - 10)
        painter.setBrush(QBrush(QColor(0, 0, 0, 180)))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rounded_rect, 10, 10)

    def show(self):
        screen_geometry = QApplication.desktop().availableGeometry()
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
            QApplication.quit()

def main():
    app = QApplication(sys.argv)
    w = Welcome()
    w.show()
    app.exec_()
