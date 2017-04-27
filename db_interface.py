# -*- coding: utf-8 -*-

import sqlite3, time, os


class mydb(object):
    def __init__(self):
        databasefile = self.initdb_file()
        self.conn = sqlite3.connect(databasefile)
        self.initdb()

    def initdb_file(self):
        cpath = os.getcwd()
        if not os.path.exists('mydata'):
            os.mkdir("mydata")
        databasefile = cpath + '\\mydata\\mydb.db'
        return databasefile

    def initdb(self):
        cu = self.conn.cursor()
        cu.execute('''CREATE TABLE  if not exists customer ( id INTEGER NOT NULL PRIMARY KEY autoincrement,
                 name varchar(20) NOT NULL,
                 sex varchar(4) DEFAULT NULL,
                 age int(11) DEFAULT NULL,
                 phone varchar(20) DEFAULT NULL,
                 job varchar(20) DEFAULT NULL,
                 address varchar(200) DEFAULT NULL,
                 email varchar(200) DEFAULT NULL,
                 desc1 varchar(200) DEFAULT NULL
               )''')


        cu.execute('''CREATE TABLE if not exists user (
             id INTEGER NOT NULL PRIMARY KEY autoincrement,
             name varchar(20) NOT NULL,
              password varchar(20) NOT NULL,
             utype varchar(20)
           )''')

        cu.execute('''CREATE TABLE if not exists user_plan (
             id INTEGER NOT NULL PRIMARY KEY autoincrement,
             customer_id int(11) ,
             state varchar(10),
             startdate date ,
             endate date ,
             priority 	int(10),
             operator varchar(20)
           )''')

        cu.execute("select * from user where name = 'admin'")
        if not cu.fetchone():
            cu.execute("insert into user (name,password,utype) values (?,?,?)", ('admin', 'admin', ''))
            self.conn.commit()


    def getadminuser(self, name, password):
        result = self.conn.cursor().execute("select * from user where name = ? and password = ?",
                                            [name, password]).fetchone()
        return result


    def insertcustomer(self, cust):
        #        [name, sex, age, phone, job, address, email, desc1]
        cu = self.conn.cursor()
        cu.execute('insert into customer (name,sex, age, phone, job, address, email, desc1)  values (?,?,?,?,?,?,?,?)',
                   cust)
        self.conn.commit()
        cu.close()
        self.close_conn()


    def updatecustomer(self, cust, cust_id):
        cust = list(cust)
        cust.append(cust_id)
        cu = self.conn.cursor()
        print cust
        cu.execute('update customer set name =?,sex=?, age=?, phone=?, job=?, address=?, email=?, desc1=? where id = ?',
                   cust)
        self.conn.commit()
        cu.close()
        self.close_conn()


    def deletecustomer(self, cust_id):
        cu = self.conn.cursor()
        sql_text = "delete from  customer where id= %d " % (cust_id)
        cu.execute(sql_text)
        self.conn.commit()
        cu.close()
        self.close_conn()


    def getcustomer(self, column_name, value):
        sql_text = "select * from customer where %s like %s " % (column_name, '\'' + '%' + value + '%' + '\'')
        result = self.conn.cursor().execute(sql_text).fetchall()
        return result


    def getcustplan(self):
        sql_text = "select a.*,b.id from customer a,user_plan b where a.id = b.customer_id  and b.state = '0' and datetime(b.startdate)<datetime('now','localtime')"
        #        sql_text="select datetime(startdate)<datetime('now','localtime')  from user_plan"
        result = self.conn.cursor().execute(sql_text).fetchall()
        return result


    def update_cust_plan(self, cust):
        current_plan = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'admin', cust[0]]
        print cust
        print current_plan
        cu = self.conn.cursor()
        cu.execute('update user_plan set state="1", endate=?, operator=? where id = ?', current_plan)
        self.conn.commit()
        cu.close()


    def insert_cust_plan(self, cust):
        current_plan = [cust[0], '0', cust[1], '', '', 'admin']
        print cust
        print current_plan
        cu = self.conn.cursor()
        cu.execute('INSERT INTO user_plan (customer_id,state,startdate,endate,priority,operator ) VALUES (?,?,?,?,?,?)',
                   current_plan)
        self.conn.commit()
        cu.close()


    def close_conn(self):
        self.conn.close()

if __name__ == '__main__':
    dd = mydb()
    #    customer1=[u'admin', u'男', 21, 15711331122, u'CLeaner', u'北京', u'', u'']
    #    dd.insertcustomer(customer1)
    #    cust=dd.getcustomer(u'name', u'kk')
    #    print cust
    #    dd.deletecustomer(2)

    #    print (dd.getcustplan())
    dd.update_cust_plan((1, 'kk', 'll', None, None, None, None, None, None, 1))
