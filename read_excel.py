# -*- coding: utf-8 -*-
import xlrd,string
from db_interface import mydb

class xlstodb():
    def __init__(self, file):
        self.import_excel_to_database(file)

    def open_excel(self,file):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception,e:
            print str(e)


    def excel_table_byname(self,file,colnameindex=0,by_name=u'客户信息'):
        data = self.open_excel(file)
        table = data.sheet_by_name(by_name)
        nrows = table.nrows #行数
#        colnames =  table.row_values(colnameindex) #某一行数据
        list =[]
        for rownum in range(1,nrows):
             row = table.row_values(rownum)
             list.append(row)
        return list

    def import_excel_to_database(self, file):
       sldb = mydb()
       cust = self.excel_table_byname(file)
       for row in cust:
           if not sldb.getcustomer('name',row[0]):
               sldb.insertcustomer(row)

       cust_plan = self.excel_table_byname(file, by_name=u'客户计划')
       for row in cust_plan:
           tt=string.replace(row[1],'/','-')+' 8:00:00'
           if sldb.getcustomer('name', row[0]):
               cust=(sldb.getcustomer('name',row[0])[0][0],tt)
               sldb.insert_cust_plan(cust)

if __name__=="__main__":
    imp=xlstodb()
    imp.import_excel_to_database()
