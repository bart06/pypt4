#!/usr/bin/python
# -*- coding: utf-8 -*-

# checkbox.py

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Checkbox')

        self.cb = QtGui.QCheckBox('Show title', self)
        #禁用 QCheckBox 的焦点
        self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb.move(10, 10)
        self.cb.toggle()
        #连接用户定义的 changeTitle() 到 stateChanged() 信号。
        # changeTitle() 方法将切换窗口标题
        self.connect(self.cb, QtCore.SIGNAL('stateChanged(int)'),
            self.changeTitle)

    def changeTitle(self, value):

        if self.cb.isChecked():
            self.setWindowTitle('Checkbox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
