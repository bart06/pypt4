CREATE TABLE customer (
     id int(11) NOT NULL,
     name varchar(20) NOT NULL,
     sex varchar(4) DEFAULT NULL,
     age int(11) DEFAULT NULL,
     phone varchar(20) DEFAULT NULL,
     job varchar(20) DEFAULT NULL,
     address varchar(200) DEFAULT NULL,
	 email varchar(200) DEFAULT NULL,
	 desc1 varchar(200) DEFAULT NULL,						
     PRIMARY KEY (id)
   );
   
CREATE TABLE user (
     id int(11) NOT NULL,
     name varchar(20) NOT NULL,
	 pasword varchar(20) NOT NULL,
     utype varchar(20) ,	 
     PRIMARY KEY (id)
   );
   
CREATE TABLE user_plan (
     id int(11) NOT NULL,
	 customer_id int(11) ,
	 state varchar(10), 
     startdate date ,
	 endate date ,
     priority 	int(10), 
	 operator varchar(20),
     PRIMARY KEY (id)  
   );
   
insert into user values (1,'admin','admin',null);