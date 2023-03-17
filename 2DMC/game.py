from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QCursor, QPixmap
from PyQt5.QtCore import Qt
import sys, csv, subprocess

p = subprocess.Popen(['python', '2DMC/mapcreate.py'], stderr=subprocess.PIPE)

output, _ = p.communicate() # Wait for the subprocess to complete and get its output
p.terminate() # Print the output and exit

load = []
terrainLoad = open('2DMC/terrainData.csv', 'r', encoding='utf-8')

reader = csv.reader(terrainLoad)
for row in reader:
    load.append(row)

TerrainOne, TerrainTwo, TerrainThree, CaveMap, hotbar, inventory = [list(row) for row in load]

def main():
    global app
    app = QApplication([])
    window = QWidget()
    layout = QHBoxLayout()

    logo = QLabel(window)
    logo.setPixmap(QPixmap('./2DMC/logo.jpg'))
    logo.setFixedSize(20, 20)
    
    title = QLabel(window)
    title.setText('MC 2D Sandbox')
    title.move(35, 5)

    window.setCursor(QCursor(QPixmap('./2DMC/cursor.cur'), 8, 3))
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.setFixedSize(900, 600)

    xButton = QPushButton(QIcon('./2DMC/xbutton.png'), '')
    xButton.setStyleSheet('QPushButton { border: none; }')
    xButton.setFixedSize(23, 23)
    xButton.clicked.connect(onXClick)

    layout.addWidget(logo, 0,  Qt.AlignTop | Qt.AlignLeft)
    layout.addWidget(xButton, 0, Qt.AlignTop | Qt.AlignRight)

    window.setLayout(layout)

    window.show()
    app.exec_()

def onXClick(): app.exit()

if __name__ == '__main__':
    main()