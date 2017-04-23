# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\eric6\w_customer.ui'
#
# Created: Thu Apr 20 22:58:13 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
from db_interface import mydb
from Ui_MainW1 import MyQQ

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class customer_Dialog(object):
    def setupUi(self, Dialog, onecust=[None, None,None,None,None,None,None,None, None]):
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 284)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 239, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 239, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 239, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 239, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setSizeGripEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pix/bird.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton_ok = QtGui.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(230, 250, 75, 23))
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(310, 250, 75, 23))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 230, 381, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(100, 250, 110, 22))
        self.dateEdit.setDisplayFormat("yyyy/MM/dd")
        self.dateEdit.setDate(QtCore.QDate.currentDate ())
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_tipdate = QtGui.QLabel(Dialog)
        self.label_tipdate.setGeometry(QtCore.QRect(10, 250, 91, 21))
        self.label_tipdate.setObjectName(_fromUtf8("label_tipdate"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 360, 191))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_work = QtGui.QLabel(self.gridLayoutWidget)
        self.label_work.setObjectName(_fromUtf8("label_work"))
        self.gridLayout.addWidget(self.label_work, 1, 2, 1, 1)
        self.label_sex = QtGui.QLabel(self.gridLayoutWidget)
        self.label_sex.setObjectName(_fromUtf8("label_sex"))
        self.gridLayout.addWidget(self.label_sex, 0, 2, 1, 1)
        self.label_nl = QtGui.QLabel(self.gridLayoutWidget)
        self.label_nl.setObjectName(_fromUtf8("label_nl"))
        self.gridLayout.addWidget(self.label_nl, 1, 0, 1, 1)
        self.lineEdit_age = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_age.setReadOnly(True)
        self.lineEdit_age.setObjectName(_fromUtf8("lineEdit_age"))
        self.gridLayout.addWidget(self.lineEdit_age, 1, 1, 1, 1)
        self.lineEdit_name = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.lineEdit_work = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_work.setReadOnly(True)
        self.lineEdit_work.setObjectName(_fromUtf8("lineEdit_work"))
        self.gridLayout.addWidget(self.lineEdit_work, 1, 3, 1, 1)
        self.lineEdit_sex = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_sex.setReadOnly(True)
        self.lineEdit_sex.setObjectName(_fromUtf8("lineEdit_sex"))
        self.gridLayout.addWidget(self.lineEdit_sex, 0, 3, 1, 1)
        self.label_adress = QtGui.QLabel(self.gridLayoutWidget)
        self.label_adress.setObjectName(_fromUtf8("label_adress"))
        self.gridLayout.addWidget(self.label_adress, 3, 0, 1, 1)
        self.label_name = QtGui.QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.label_phone = QtGui.QLabel(self.gridLayoutWidget)
        self.label_phone.setObjectName(_fromUtf8("label_phone"))
        self.gridLayout.addWidget(self.label_phone, 2, 0, 1, 1)
        self.label_7desc = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7desc.setObjectName(_fromUtf8("label_7desc"))
        self.gridLayout.addWidget(self.label_7desc, 4, 0, 1, 1)
        self.lineEdit_phone = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_phone.setReadOnly(True)
        self.lineEdit_phone.setObjectName(_fromUtf8("lineEdit_phone"))
        self.gridLayout.addWidget(self.lineEdit_phone, 2, 1, 1, 3)
        self.lineEdit_adress = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_adress.setReadOnly(True)
        self.lineEdit_adress.setObjectName(_fromUtf8("lineEdit_adress"))
        self.gridLayout.addWidget(self.lineEdit_adress, 3, 1, 1, 3)
        self.textEdit_desc = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_desc.setReadOnly(True)
        self.textEdit_desc.setObjectName(_fromUtf8("textEdit_desc"))
        self.gridLayout.addWidget(self.textEdit_desc, 4, 1, 1, 3)
        self.dlg=Dialog
        self.current_customer=[None, None,None,None,None,None,None,None, None]
        if  onecust:
            self.current_customer=onecust
#            print self.customer
            self.lineEdit_name.setText(_translate("Dialog", unicode(self.current_customer[1]), None))
            self.lineEdit_sex.setText(_translate("Dialog", unicode(self.current_customer[2]), None))
            self.lineEdit_age.setText(_translate("Dialog",unicode(self.current_customer[3])  , None))
            self.lineEdit_work.setText(_translate("Dialog",unicode(self.current_customer[5]), None))
            self.lineEdit_phone.setText(_translate("Dialog", unicode(self.current_customer[4]), None))  
            self.lineEdit_adress.setText(_translate("Dialog",unicode(self.current_customer[6]), None))
            self.textEdit_desc.setText(_translate("Dialog", unicode(self.current_customer[8]), None))
    
        self.mainw=None
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accept)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "客户提示计划", None))
        self.label_tipdate.setText(_translate("Dialog", "下次提醒时间 ：", None))
        self.groupBox.setTitle(_translate("Dialog", "客户信息", None))
        self.label_work.setText(_translate("Dialog", "工作 ：", None))
        self.label_sex.setText(_translate("Dialog", "性别 ：", None))
        self.label_nl.setText(_translate("Dialog", "年龄 ：", None))
        self.label_adress.setText(_translate("Dialog", "地址 ：", None))
        self.label_name.setText(_translate("Dialog", "姓名 ：", None))
        self.label_phone.setText(_translate("Dialog", "电话 ：", None))
        self.label_7desc.setText(_translate("Dialog", "备注 ：", None))
        self.pushButton_ok.setText(_translate("Dialog", "确定", None))
        self.pushButton_cancel.setText(_translate("Dialog", "取消", None))
        print(Dialog)
    

    def  accept(self):

        if not self.current_customer[0]:
            msgBox = QMessageBox()
            msgBox.setWindowTitle(u'操作提示')
            msgBox.setText(u'未找到要操作的记录！')
            msgBox.setStandardButtons(QMessageBox.Yes)
            msgBox.exec_()
            self.dlg.hide()

            
        elif  self.dateEdit.date()==QtCore.QDate.currentDate():
            sqldb=mydb()
            sqldb.update_cust_plan(self.current_customer)
            self.mainw=MyQQ()
            self.mainw.show()
            self.dlg.hide()
            
        elif  self.dateEdit.date()>QtCore.QDate.currentDate():
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u'操作提示')
            msgBox.setText(u'是否要添加提示计划？')
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
            msgBox.setDefaultButton(QMessageBox.Yes);
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                sqldb=mydb()
                sqldb.update_cust_plan(self.current_customer)
                sqldb.insert_cust_plan([self.current_customer[0],unicode(self.dateEdit.date().toString("yyyy/MM/dd"))])
                self.mainw=MyQQ()
                self.mainw.show()
                self.dlg.hide()
            
      

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = customer_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

