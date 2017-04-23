# coding=utf-8
import sys, time
from PyQt4.QtCore import *
from PyQt4.QtGui import *



class Mybutton(QWidget):
    def __init__(self, parent=None):
        super(Mybutton, self).__init__(parent)
        self.resize(200, 100)
        self.setWindowTitle("QTimerDemo")

        self.toolButton=QToolButton()  
        self.toolButton.setText(u"小李") 
        self.toolButton.setIcon(QIcon("pix/woman_d.gif"))  

        layout = QVBoxLayout()
        layout.addWidget(self.toolButton)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.start()

        # 信号连接到槽
        self.timer.timeout.connect(self.onTimerOut)
        print dir(self.toolButton)
    # 定义槽
        self.aa=True
    def onTimerOut(self):
        a_path="pix/wu.gif"
        b_path="pix/woman_d.gif"
        if self.aa :
            self.toolButton.setIcon(QIcon(a_path))
            self.aa=False
        else:
            self.toolButton.setIcon(QIcon(b_path))
            self.aa=True
        

app = QApplication(sys.argv)
t = Mybutton()
t.show()
sys.exit(app.exec_())
