#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

'''显示了一个LCD数字和一个滑块，
  通过拖动滑块来改变LCD的值'''

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        #改变数字，及显示数字
        self.connect(slider,  QtCore.SIGNAL('valueChanged(int)'), lcd,
            QtCore.SLOT('display(int)'))

        self.setWindowTitle('Signal & slot')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
