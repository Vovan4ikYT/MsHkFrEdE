import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Mshkfrede(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setGeometry(50, 50, 500, 500)
        self.draw_flag = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.draw_flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.draw_flag = True
        self.repaint()

    def draw(self, qp):
        size = randint(20, 100)
        color = QColor(255, 255, 0)
        qp.setBrush(color)
        qp.drawEllipse(randint(0, 500) - size // 2, randint(0, 500) - size // 2, size, size)
        self.draw_flag = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mshkfrede()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
