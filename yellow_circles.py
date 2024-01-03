import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import  QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow_circles.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.setWindowTitle('Окружности')
    
    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        h = random.randint(5, 50)
        qp.drawEllipse(random.randint(30, 270), random.randint(30, 270), h, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())