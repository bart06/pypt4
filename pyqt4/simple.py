#coding:utf-8
#!/usr/bin/python

# simple.py
import sys
from PyQt4 import QtGui, QtCore

class mainw(QtGui.QWidget):
    
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('登录') #设置标题
        self.resize(250, 150) #设置大小
        self.setWindowIcon(QtGui.QIcon('icons/bird.png')) #设置图标
        self.center()  # 设置居中
        
        #设置提示及字体
        self.setToolTip('This is a <b>QWidget</b> widget')
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))
        
        #增加按钮
        self.quit_button = QtGui.QPushButton("Close", self)
        self.quit_button.setGeometry(10, 10, 64, 35)
        
        
        #设置信号槽，给quit按钮增加clicked的事件为退出
        self.connect(self.quit_button, QtCore.SIGNAL('clicked()'),QtGui.qApp, QtCore.SLOT('quit()'))

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    

app = QtGui.QApplication(sys.argv)
main = mainw()
main.show()
sys.exit(app.exec_())
