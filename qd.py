from Ui_message_ok import Message_Dialog
from PyQt4 import QtGui
import sys
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Message_Dialog()
ui.setupUi(Dialog, 'new')
Dialog.show()
sys.exit(app.exec_())
