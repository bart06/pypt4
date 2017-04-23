import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        #设置窗口大小
        self.resize(250, 150)
        #设置窗口标题
        self.setWindowTitle('statusbar')
        
        #设置退出，快捷键，提示，及事件
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        #更新状态栏
        self.statusBar()
        #设置菜单栏
        menubar = self.menuBar()
        #加入file项目
        file = menubar.addMenu('&File')
        #加入退出键
        file.addAction(exit)
        
        #设置工具栏
        self.toolbar = self.addToolBar('Exit')
        #加入退出键
        self.toolbar.addAction(exit)
        
        #工具栏
        self.statusBar().showMessage('Ready')


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
