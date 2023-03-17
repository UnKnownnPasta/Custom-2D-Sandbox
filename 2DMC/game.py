from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QCursor, QPixmap
from PyQt5.QtCore import Qt
import sys, csv, subprocess, os

p = subprocess.Popen(['python', '2DMC/mapcreate.py'], stderr=subprocess.PIPE)

output, _ = p.communicate() # Wait for the subprocess to complete and get its output
p.terminate() # Print the output and exit

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

load = []
terrainLoad = open('2DMC/terrainData.csv', 'r', encoding='utf-8')

reader = csv.reader(terrainLoad)
for row in reader:
    load.append(row)

TerrainOne, TerrainTwo, TerrainThree, CaveMap, hotbar, inventory = [list(row) for row in load]

class CloseButton(QPushButton):
    def __init__(self, text=None, parent=None):
        super(CloseButton, self).__init__(text, parent)
        self.setIcon(QIcon('./2DMC/assets/xbutton.png'))
        self.setStyleSheet('QPushButton { border: none; }')
        self.setFixedSize(23, 23)
        self.clicked.connect(self.onXClick)
    
    def enterEvent(self, event):
        self.setStyleSheet("QPushButton { border-style: solid; border-width: 1px; border-color: black; background-color: rgba(211, 211, 211, 0.7); }")
    
    def leaveEvent(self, event):
        self.setStyleSheet("QPushButton { border: none; background-color: none; }")

    def onXClick(self, x): app.exit()

class MaxMinButton(QPushButton):
    def __init__(self, icon, text=None):
        super(MaxMinButton, self).__init__(icon, text)
        # self.setIcon(QIcon('./2DMC/assets/Min.png'))
        self.setStyleSheet('QPushButton { border: none; }')
        self.setFixedSize(23, 23)
        self.clicked.connect(self.onMinMaxClick)

    def enterEvent(self, event):
        self.setStyleSheet("QPushButton { border-style: solid; border-width: 1px; border-color: black; background-color: rgba(211, 211, 211, 0.7); }")
    
    def leaveEvent(self, event):
        self.setStyleSheet("QPushButton { border: none; background-color: none; }")

    def onMinMaxClick(self):
        if window.windowState() == Qt.WindowMaximized:
            window.setWindowState(Qt.WindowMinimized)
            self.deleteLater()
            layout.addWidget(MaxMinButton(QIcon('./2DMC/assets/Min.png')), 0, Qt.AlignTop | Qt.AlignRight)
        else:
            window.setWindowState(Qt.WindowMaximized)
            self.deleteLater()
            layout.addWidget(MaxMinButton(QIcon('./2DMC/assets/Max.png')), 0, Qt.AlignTop | Qt.AlignRight)

class GameWindow(QWidget):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.setCursor(QCursor(QPixmap('./2DMC/assets/cursor.cur'), 8, 3))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(900, 600)


def main():
    global app, window, layout, b1
    app = QApplication([])
    window = GameWindow()
    layout = QHBoxLayout()
    layout.setSpacing(0)
    layout.addStretch(1)

    b1 = MaxMinButton(QIcon('./2DMC/assets/Min.png'))

    logo = QLabel(window)
    logo.setPixmap(QPixmap('./2DMC/assets/logo.jpg'))
    logo.setFixedSize(20, 20)
    logo.move(11, 11)
    
    title = QLabel(window)
    title.setText('MC 2D Sandbox')
    title.move(35, 5)

    layout.addWidget(CloseButton(), 0, Qt.AlignTop | Qt.AlignRight)
    layout.addWidget(b1, 0, Qt.AlignTop | Qt.AlignRight)

    window.setLayout(layout)


if __name__ == '__main__':
    main()
    
    window.show()
    app.exec_()