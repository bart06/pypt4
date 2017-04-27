# -*- coding: utf-8 -*- 
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import os.path
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
        
class MyButton(QtGui.QToolButton):
    def __init__(self, _id, *args, **kwargs):
        self._id = _id
        QtGui.QPushButton.__init__(self, *args, **kwargs)
        
  
class MyQQ(QTabWidget):  
    def __init__(self,parent=None):  
        super(MyQQ,self).__init__(parent)  
        self.setWindowTitle(u"客户系统")
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pix/bird.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.current_custmer_name=None
        self.current_custmer=[]
        
        #加入客户操作编辑类
        from Ui_OperateM1 import Ui_OperateDialog
        self.dg_operator=QtGui.QDialog()
        self.opt_cust = Ui_OperateDialog()
        self.opt_cust.setupUi(self.dg_operator)
        
        
        from Ui_w_customer1 import customer_Dialog
        self.dg_customer=QtGui.QDialog()
        self.optDg = customer_Dialog()
        
        
        
        groupbox1=QGroupBox()  
        self.vlayout1=QVBoxLayout(groupbox1)  
        self.vlayout1.setMargin(10)  
        self.vlayout1.setAlignment(Qt.AlignCenter)           
        
        #动态添加图标
        from db_interface import mydb
        sqldb=mydb()
        self.cust=sqldb.getcustplan()
#        print self.cust
        for cust_i in self.cust:

            self.toolButton=MyButton(cust_i[0])  
            self.toolButton.setText(unicode(cust_i[1]))
            pik=''
            if unicode(cust_i[2])==u'男':
                pik="pix/man.png"
            else:
                pik="pix/woman.png"
            self.icon=QIcon(pik)
            self.toolButton.setIcon(self.icon)
            self.toolButton.setIconSize(QSize(60,60))  
            self.toolButton.setAutoRaise(True)  
            self.toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            self.connect( self.toolButton , QtCore.SIGNAL("clicked()"), self.onecust_clicked)
            self.vlayout1.addWidget(self.toolButton)     
            
        #拉伸
        self.vlayout1.addStretch()
        
        self.toolButton_modify=QPushButton()  
        self.toolButton_modify.setText(self.tr(u"客户信息编辑"))  
        self.toolButton_modify.setIcon(QIcon("pix/modify.png"))  
        self.toolButton_modify.setIconSize(QSize(40,40))  
#        toolButton_modify.setAutoRaise(True)  
#        toolButton_modify.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        self.toolButton_select=QPushButton()  
        self.toolButton_select.setText(self.tr(u"数据导入"))  
        self.toolButton_select.setIcon(QIcon("pix/takein.png"))  
        self.toolButton_select.setIconSize(QSize(40,40))  
#        toolButton_select.setAutoRaise(True)  
#        toolButton_select.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        groupbox2=QGroupBox()  
        vlayout2=QVBoxLayout(groupbox2)  
        vlayout2.setMargin(10)  
        vlayout2.setAlignment(Qt.AlignCenter)   
        vlayout2.addWidget(self.toolButton_modify)
        vlayout2.addWidget(self.toolButton_select)   
        vlayout2.addStretch()  
  
        self.toolbox1 = QToolBox()  
        self.toolbox1.addItem(groupbox1,u"我的客户")  
        self.toolbox1.addItem(groupbox2,self.tr("功能"))
                 
          
        self.addTab(self.toolbox1, u"联系人") 
        #到边上
        self.toside()
            
        self.toolButton_modify.clicked.connect(self.modify_customer) 
        self.toolButton_select.clicked.connect(self.import_customer)
            
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.start()

        # 信号连接到槽
        self.timer.timeout.connect(self.onTimerOut)

    # 定义槽
        self.show_flag=True
    def onTimerOut(self):
        
        if self.show_flag :
            for tb in self.findChildren(QToolButton):
                tb.setIcon(QIcon("pix/wu.png")) 
            self.show_flag=False
        else:
            for tb in self.findChildren(QToolButton):
                for cust in self.cust:
                    if unicode(tb.text())==cust[1]:
                        if unicode(cust[2])==u'男':
                            pik="pix/man.png"
                        else:
                            pik="pix/woman.png"
                        tb.setIcon(QIcon(pik)) 
            self.show_flag=True
            
    def modify_customer(self):
        self.dg_operator.show()
        
    def import_customer(self):
        print 'import_customer'
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './*.xls', '.xls')
        path,file=os.path.split(unicode(filename)); 
        if file==u'客户导入模板.xls':
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u'操作提示')
            msgBox.setText(u'是否要导入客户信息？')
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
            msgBox.setDefaultButton(QMessageBox.Yes);
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                from read_excel import  xlstodb
                xlstodb(unicode(filename))
                msgBox.setText(u'导入完成')
                msgBox.setStandardButtons(QMessageBox.Yes);
                msgBox.exec_()
    
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u'操作提示')
            msgBox.setText(u'您选择的不是指定的模板文件')
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
            msgBox.setDefaultButton(QMessageBox.Yes);
            msgBox.exec_()      
            
        
    def onecust_clicked(self):
        onecust=[]
        for cust in self.cust:
            if cust[0]==self.sender()._id:    
                onecust=cust
        self.optDg.setupUi(self.dg_customer, onecust)
        self.dg_customer.show()
        self.hide()

    
    
    def toside(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
#        self.move((screen.width()-size.width()) , (screen.height()-size.height()))
        self.setGeometry ((screen.width()-size.width())+320 , (screen.height()-size.height())-130, 200, 390)
    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myqq=MyQQ()  
    myqq.show()  
    app.exec_()
    sys.exit(app.exec_())

