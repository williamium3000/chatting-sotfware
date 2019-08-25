import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget
from PyQt5.QtCore import pyqtSignal,QObject

class Communication(QObject):
    closeApp = pyqtSignal()

class EmitSignal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communication()
        self.c.closeApp.connect(self.close)

        self.resize(250, 150)
        self.setWindowTitle("发射信号演示程序") 
        self.show()

    def mousePressEvent(self, QMouseEvent):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    es = EmitSignal()
    sys.exit(app.exec_())