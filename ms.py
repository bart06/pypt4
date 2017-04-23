from PyQt4 import QtGui, QtCore
from Ui_MainW1 import MyQQ
import sys
app = QtGui.QApplication(sys.argv)
myqq=MyQQ()  
myqq.show()  
app.exec_()
#sys.exit(app.exec_())
