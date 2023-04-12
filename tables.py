import mysql.connector as sql
conn= sql.connect(host='localhost', user = 'root', password ='1234')
c1=conn.cursor()
c1.execute('create database marriage_bureau_system')

c1.execute('create table legends_details(name varchar (200),address varchar(20),caste varchar (100),appearence varchar(100),age bigint(55),profession varchar (255),phone_no  bigint(200)')
c1.execute('create girls_details(name varchar(100),address varchar(100),caste varchar(50),appearence varchar(25),age int(4),profession varchar(65),phone_no varchar(15)')
c1.execute('create table user_id(user_name varchar(55),password varchar(55)')
conn.commit()
