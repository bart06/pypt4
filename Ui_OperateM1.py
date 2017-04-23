# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\eric6\OperateM.ui'
#
# Created: Sat Mar 25 18:30:34 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from db_interface import mydb
import sys


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

class Ui_OperateDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pix/bird.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.resize(600, 400)
        Dialog.setFixedSize(600, 400)  #固定大小，不可调
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
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(True)
        self.button_ok= QtGui.QPushButton(Dialog)
        self.button_ok.setGeometry(QtCore.QRect(450, 360, 65, 21))
        self.button_cancel= QtGui.QPushButton(Dialog)
        self.button_cancel.setGeometry(QtCore.QRect(520, 360, 65, 21))
        self.groupBox_select = QtGui.QGroupBox(Dialog)
        self.groupBox_select.setGeometry(QtCore.QRect(10, 10, 571, 51))
        self.groupBox_select.setObjectName(_fromUtf8("groupBox_select"))
        self.label = QtGui.QLabel(self.groupBox_select)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_cx = QtGui.QLineEdit(self.groupBox_select)
        self.lineEdit_cx.setGeometry(QtCore.QRect(110, 20, 113, 20))
        self.lineEdit_cx.setObjectName(_fromUtf8("lineEdit_cx"))
        self.groupBox_selecttype = QtGui.QGroupBox(self.groupBox_select)
        self.groupBox_selecttype.setGeometry(QtCore.QRect(300, 10, 251, 31))
        self.groupBox_selecttype.setObjectName(_fromUtf8("groupBox_selecttype"))
        self.radioButton_xm = QtGui.QRadioButton(self.groupBox_selecttype)
        self.radioButton_xm.setGeometry(QtCore.QRect(50, 10, 51, 16))
        self.radioButton_xm.setObjectName(_fromUtf8("radioButton_xm"))
        self.radioButton_dq = QtGui.QRadioButton(self.groupBox_selecttype)
        self.radioButton_dq.setGeometry(QtCore.QRect(110, 10, 51, 16))
        self.radioButton_dq.setObjectName(_fromUtf8("radioButton_dq"))
        self.radioButton_bz = QtGui.QRadioButton(self.groupBox_selecttype)
        self.radioButton_bz.setGeometry(QtCore.QRect(170, 10, 71, 16))
        self.radioButton_bz.setObjectName(_fromUtf8("radioButton_bz"))
        self.pushButton_cx = QtGui.QPushButton(self.groupBox_select)
        self.pushButton_cx.setGeometry(QtCore.QRect(230, 18, 61, 23))
        self.pushButton_cx.setObjectName(_fromUtf8("pushButton_cx"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(140, 70, 441, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 401, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_xm = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_xm.setObjectName(_fromUtf8("lineEdit_xm"))
        self.gridLayout.addWidget(self.lineEdit_xm, 0, 1, 1, 1)
        self.comboBox_xb = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_xb.setObjectName(_fromUtf8("comboBox_xb"))
        self.comboBox_xb.addItem(_fromUtf8(""))
        self.comboBox_xb.addItem(_fromUtf8(""))
        self.comboBox_xb.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_xb, 0, 3, 1, 1)
        self.lineEdit_tel = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_tel.setObjectName(_fromUtf8("lineEdit_tel"))
        self.gridLayout.addWidget(self.lineEdit_tel, 1, 3, 1, 1)
        self.lineEdit_email = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_email.setObjectName(_fromUtf8("lineEdit_email"))
        self.gridLayout.addWidget(self.lineEdit_email, 3, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.lineEdit_nl = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_nl.setObjectName(_fromUtf8("lineEdit_nl"))
        self.gridLayout.addWidget(self.lineEdit_nl, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.lineEdit_gz = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_gz.setObjectName(_fromUtf8("lineEdit_gz"))
        self.gridLayout.addWidget(self.lineEdit_gz, 3, 1, 1, 1)
        self.lineEdit_dz = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_dz.setObjectName(_fromUtf8("lineEdit_dz"))
        self.gridLayout.addWidget(self.lineEdit_dz, 2, 1, 1, 3)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.textEdit_bz = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_bz.setObjectName(_fromUtf8("textEdit_bz"))
        self.gridLayout.addWidget(self.textEdit_bz, 4, 1, 1, 3)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(140, 350, 251, 31))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButton_new = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_new.setGeometry(QtCore.QRect(70, 10, 60, 16))
        self.radioButton_new.setObjectName(_fromUtf8("radioButton_new"))
        self.radioButton_modify = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_modify.setGeometry(QtCore.QRect(130, 10, 51, 16))
        self.radioButton_modify.setObjectName(_fromUtf8("radioButton_modify"))
        self.radioButton_delete = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_delete.setGeometry(QtCore.QRect(190, 10, 51, 16))
        self.radioButton_delete.setObjectName(_fromUtf8("radioButton"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 70, 120, 311))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tableView = QtGui.QTableView(self.groupBox_3)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 101, 281))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.cust=[]
        self.current_customer=[]
        self.current_customer_id=None
        

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.button_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_button_ok_accepted)
        QtCore.QObject.connect(self.button_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.radioButton_xm, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_radioButton_xm_clicked)
        QtCore.QObject.connect(self.radioButton_dq, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_radioButton_dq_clicked)
        QtCore.QObject.connect(self.radioButton_bz, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_radioButton_bz_clicked)
        QtCore.QObject.connect(self.radioButton_new, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_radioButton_new_clicked)
        QtCore.QObject.connect(self.radioButton_modify, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_radioButton_modify_clicked)
        QtCore.QObject.connect(self.radioButton_delete, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_radioButton_delete_clicked)
        QtCore.QObject.connect(self.pushButton_cx, QtCore.SIGNAL(_fromUtf8("clicked()")), self.on_pushButton_cx_clicked)
        QtCore.QObject.connect(self.tableView,SIGNAL("doubleClicked(const QModelIndex&)"), self.on_tableView_doubleClicked) 
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "客户信息编辑", None))
        self.groupBox_select.setTitle(_translate("Dialog", "查询", None))
        self.label.setText(_translate("Dialog", "按姓名查询：", None))
        self.groupBox_selecttype.setTitle(_translate("Dialog", "按类型", None))
        self.radioButton_xm.setText(_translate("Dialog", "姓名", None))
        self.radioButton_xm.setChecked(True)
        self.radioButton_dq.setText(_translate("Dialog", "地区", None))
        self.radioButton_bz.setText(_translate("Dialog", "备注信息", None))
        self.groupBox.setTitle(_translate("Dialog", "客户明细信息", None))
        self.label_2.setText(_translate("Dialog", "姓 名 ：", None))
        self.label_4.setText(_translate("Dialog", "年 龄 :", None))
        self.label_7.setText(_translate("Dialog", "工 作 ：", None))
        self.label_6.setText(_translate("Dialog", "地 址 ：", None))
        self.label_5.setText(_translate("Dialog", "电 话 ：", None))
        self.label_3.setText(_translate("Dialog", "性 别 ：", None))
        self.label_8.setText(_translate("Dialog", "电子邮件 ： ", None))
        self.label_9.setText(_translate("Dialog", "备注信息 ： ", None))
        self.groupBox_2.setTitle(_translate("Dialog", "功能选择 ", None))
        self.radioButton_new.setText(_translate("Dialog", "新增", None))
        self.radioButton_modify.setText(_translate("Dialog", "修改", None))
        self.radioButton_delete.setText(_translate("Dialog", "删除", None))
        self.groupBox_3.setTitle(_translate("Dialog", "点击查看详细信息", None))
        self.pushButton_cx.setText(_translate("Dialog", "查询", None))
        self.comboBox_xb.setItemText(0, _translate("select", "请选择", None))
        self.comboBox_xb.setItemText(1, _translate("select", "男", None))
        self.comboBox_xb.setItemText(2, _translate("select", "女", None))
        self.button_ok.setText(u'确定')
        self.button_cancel.setText(u'取消')
        self.read_only_true()
        
        
    def read_only_true(self):
        self.lineEdit_xm.setReadOnly(True)
        self.comboBox_xb.setEditable(False)
        self.lineEdit_nl.setReadOnly(True)
        self.lineEdit_tel.setReadOnly(True)
        self.lineEdit_gz.setReadOnly(True)
        self.lineEdit_dz.setReadOnly(True)
        self.lineEdit_email.setReadOnly(True)
        self.textEdit_bz.setReadOnly(True)
    
    def read_only_false(self):
        self.lineEdit_xm.setReadOnly(False)
        self.comboBox_xb.setEditable(True)
        self.lineEdit_nl.setReadOnly(False)
        self.lineEdit_tel.setReadOnly(False)
        self.lineEdit_gz.setReadOnly(False)
        self.lineEdit_dz.setReadOnly(False)
        self.lineEdit_email.setReadOnly(False)
        self.textEdit_bz.setReadOnly(False)
        
    def clean_text(self):
        self.lineEdit_xm.setText(u'')
        self.comboBox_xb.setCurrentIndex(0)
        self.lineEdit_nl.setText(u'')
        self.lineEdit_tel.setText(u'')
        self.lineEdit_gz.setText(u'')
        self.lineEdit_dz.setText(u'')
        self.lineEdit_email.setText(u'')
        self.textEdit_bz.setText(u'')
    def gettext(self):
        xm=unicode(self.lineEdit_xm.text())
        xb=unicode(self.comboBox_xb.currentText())
        if xb==u'请选择':
            xb=u''
        nl=unicode(self.lineEdit_nl.text())
        tel=unicode(self.lineEdit_tel.text())
        gz=unicode(self.lineEdit_gz.text())
        dz=unicode(self.lineEdit_dz.text())
        email=unicode(self.lineEdit_email.text())
        bz=unicode(self.textEdit_bz.toPlainText())
        return [xm, xb, nl, tel, gz, dz, email, bz]
    
    
    def set_text(self, cust):
        if  cust[1]:
            self.lineEdit_xm.setText(unicode(cust[1]))
        if  cust[2]:
            if cust[2]==u'男':
                self.comboBox_xb.setCurrentIndex(1)
            if cust[2]==u'女':
                self.comboBox_xb.setCurrentIndex(2)
        if  cust[3]:
            self.lineEdit_nl.setText(unicode(cust[3]))
        if  cust[4]:    
            self.lineEdit_tel.setText(unicode(cust[4]))
        if  cust[5]:     
            self.lineEdit_gz.setText(unicode(cust[5]))
        if  cust[6]: 
            self.lineEdit_dz.setText(unicode(cust[6]))
        if  cust[7]: 
            self.lineEdit_email.setText(unicode(cust[7]))
        if  cust[8]: 
            self.textEdit_bz.setText(unicode(cust[8]))
            
        self.current_customer_id=cust[0]
            
    def tableView_set(self, customer=[]):
        # 添加表头：
        self.model = QtGui.QStandardItemModel(self.tableView)
    
        
        row=len(customer)
        # 设置表格属性：
        self.model.setRowCount(row)
        self.model.setColumnCount(2)

        # 设置表头
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, _fromUtf8(u"ID"))
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, _fromUtf8(u"NAME"))

        self.tableView.setModel(self.model)

        # 设置列宽
        self.tableView.setColumnWidth(0, 30)
        self.tableView.setColumnWidth(1, 52)
        # 合并单元格的效果
        # 第一个参数：要改变的单元格行数
        # 第二个参数：要改变的单元格列数
        # 第三个参数：需要合并的行数
        # 第四个参数：需要合并的列数
        # self.tableView.setSpan(0, 2, 17, 1)
        # self.tableView.setSpan(0, 5, 17, 1)

        # 设置单元格禁止更改
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        # 表头信息显示居左
        # self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)

        # 表头信息显示居中
        self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)



        # 添加表项
        tablelist=[]
        for c in customer:
            tablelist.append(str(c[0]))
            tablelist.append(c[1])
#        print  tablelist   
        index = 0
        for i in range(0, row):
            self.model.setItem(i, 0, QtGui.QStandardItem(_fromUtf8(tablelist[index])))
            index += 1
            self.model.setItem(i, 1, QtGui.QStandardItem(_fromUtf8(tablelist[index])))
            index += 1

        self.tableView.setModel(self.model)    
    
    @pyqtSignature("")
    def on_radioButton_xm_clicked(self):
        """
        Slot documentation goes here.
        """
        self.label.setText(_translate("Dialog", "按姓名查询：", None))
        self.read_only_true()
        print '按姓名查询'
    
    @pyqtSignature("")
    def on_radioButton_dq_clicked(self):
        """
        Slot documentation goes here.
        """
        self.label.setText(_translate("Dialog", "按地区查询", None))
        self.read_only_true()
        print '按地区查询'
    
    @pyqtSignature("")
    def on_radioButton_bz_clicked(self):
        """
        Slot documentation goes here.
        """
        self.label.setText(_translate("Dialog", "按备注查询", None))
        self.read_only_true()
        print '按备注信息查询'
        
    @pyqtSignature("QModelIndex")
    def on_tableView_doubleClicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        self.current_customer= self.cust[index.row()]
        self.set_text(self.current_customer)
        
    @pyqtSignature("")
    def on_radioButton_new_clicked(self):
        self.read_only_false()
        self.clean_text()
        self.tableView_set()
    
    @pyqtSignature("")
    def on_radioButton_modify_clicked(self):
        """
        Slot documentation goes here.
        """
        self.read_only_false()
    
    @pyqtSignature("")
    def on_radioButton_delete_clicked(self):
        """
        Slot documentation goes here.
        """
        self.read_only_true()
        
    def on_pushButton_cx_clicked(self):
        
        print '开始查询'
        if self.lineEdit_cx.text()==u'':
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u'操作提示')
            msgBox.setText(u'查询内容不能为空！')
            msgBox.setStandardButtons(QMessageBox.Yes)
            msgBox.exec_()
            self.lineEdit_cx.setFocus()
        elif self.radioButton_xm.isChecked():
            sqldb=mydb()
            self.cust=sqldb.getcustomer(u'name', unicode(self.lineEdit_cx.text()))
            sqldb.close_conn()
            print self.cust
            self.tableView_set(self.cust)
        elif self.radioButton_dq.isChecked():
            sqldb=mydb()
            self.cust=sqldb.getcustomer(u'address', unicode(self.lineEdit_dz.text()))
            sqldb.close_conn()
            self.tableView_set(self.cust)
        elif self.radioButton_bz.isChecked():
            sqldb=mydb()
            self.cust=sqldb.getcustomer(u'desc1', unicode(self.textEdit_bz.text()))
            sqldb.close_conn()
            self.tableView_set(self.cust)
        
        
    @pyqtSignature("")
    def on_button_ok_accepted(self):
        """
        Slot documentation goes here.
        """
        if self.radioButton_new.isChecked():
            customer1=self.gettext()
            print customer1
            self.click_ok_operate('new', customer1)
            
#        if not self.current_customer_id:
#            msgBox = QtGui.QMessageBox()
#            msgBox.setWindowTitle(u'操作提示')
#            msgBox.setText(u'未找到要操作的记录！')
#            msgBox.setStandardButtons(QMessageBox.Yes)
#            msgBox.exec_()
#            self.lineEdit_cx.setFocus()
            
        elif self.radioButton_modify.isChecked() :
            self.click_ok_operate('modify', self.gettext())
            
        elif self.radioButton_delete.isChecked() :
            self.click_ok_operate('delete', self.gettext())
    
    
    
    def click_ok_operate(self, type, cust):
        
        if type=='new':
            if not cust[1]:
                msgBox = QtGui.QMessageBox()
                msgBox.setWindowTitle(u'操作提示')
                msgBox.setText(u'用户名不能为空！')
                msgBox.setStandardButtons(QMessageBox.Yes)
                ret = msgBox.exec_()
                self.lineEdit_xm.setFocus()
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setWindowTitle(u'操作提示')
                msgBox.setText(u'是否要添加记录？')
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
                msgBox.setDefaultButton(QMessageBox.Yes);
                ret = msgBox.exec_()
                if ret == QMessageBox.Yes:
                    sqldb=mydb()
                    sqldb.insertcustomer(cust)
                    self.clean_text()
                    
        if type=='modify':
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u'操作提示')
            msgBox.setText(u'是否要修改记录？')
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
            msgBox.setDefaultButton(QMessageBox.Yes);
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                sqldb=mydb()
                sqldb.updatecustomer(cust, self.current_customer_id)
                self.clean_text()
                
        if type=='delete':
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u'操作提示')
            msgBox.setText(u'是否要删除记录？')
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
            msgBox.setDefaultButton(QMessageBox.Yes);
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                sqldb=mydb()
                
                sqldb.deletecustomer(self.current_customer_id)
                self.clean_text()  
                self.tableView_set([])           

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_OperateDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

