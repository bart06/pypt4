# -*- coding: utf-8 -*-
import xlrd,time,string
from db_interface import mydb


def open_excel(file= u'客户导入模板.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)


def excel_table_byname(file= u'客户导入模板.xls',colnameindex=0,by_name=u'客户信息'):
    data = open_excel()
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         list.append(row)
    return list

def import_excel_to_database():
   sldb = mydb()
   cust = excel_table_byname()
   for row in cust:
       if not sldb.getcustomer('name',row[0]):
           sldb.insertcustomer(row)

   cust_plan = excel_table_byname(by_name=u'客户计划')
   for row in cust_plan:
       tt=string.replace(row[1],'/','-')+' 8:00:00'
       if sldb.getcustomer('name', row[0]):
           cust=(sldb.getcustomer('name',row[0])[0][0],tt)
           sldb.insert_cust_plan(cust)

if __name__=="__main__":
    import_excel_to_database()