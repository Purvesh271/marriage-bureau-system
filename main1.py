from prettytable import from_db_cursor
import  mysql . connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1234',database='marriage_bureau_system')
cur = conn.cursor()

print('******************************************MARRIAGE BUREAU SYSTEM****************************************')
print('1.REGISTER')
print('2.LOGIN')
n=int(input('Enter your choice:'))
if n== 1:
     name=input('Enter your  User name:')
     passwd=int(input('Enter  your  Password(only numbers):'))
     print()
     V_SQLInsert="INSERT  INTO user_id (password,user_name) values (" +  str (passwd) + ",' " + name + " ') "
     cur.execute(V_SQLInsert)
     conn.commit()
     print()
     print('USER created succesfully')
     import py

if  n==2 :
     name=input('Enter your Username=')
     print()
     passwd=int(input('Enter your  Password='))
     V_Sql_Sel="select * from user_id where password='"+str (passwd)+"' and user_name=  ' " +name+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchone() is  None:
          print()
          print('Invalid username or password')
     else:
          print()
          import py

     

