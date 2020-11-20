import sys

from PyQt5.QtGui import QPainter, QColor
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)

        self.flag = False

    def run(self):
        self.flag = True
        self.size = randint(0, 300)
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)

            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(50, 50, self.size, self.size)

            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())