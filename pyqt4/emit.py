#!/usr/bin/python
# -*- coding: utf-8 -*-

# emit.py

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        #创建的 closeEmitApp() 信号和 close() 槽连接
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'),QtCore.SLOT('close()'))

        self.setWindowTitle('emit')
        self.resize(250, 150)

    #鼠标的按下实践中发射该信号
    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('closeEmitApp()'))


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
