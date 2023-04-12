from prettytable import from_db_cursor
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1234',database='marriage_bureau_system')
if conn.is_connected():
     c1=conn.cursor()
     print('_________________________________WELCOME TO MARRIAGE BUREAU SYSTEM  __________________________________')
     c='y'
     while c.lower()=='y':
          print('=======================')
          print("1.provide details")
          print('2.in search of bride/groom')
          print('3.Loans and Advances')
          
          choice=int(input('enter the choice:'))
          if choice==1:
              print('==========================')
              print('6.Male customer details')
              print('7.Female customer details')
              choice=int(input('enter the choice:-'))
          if choice==2:
               print('========================')
               print('4. Handsome Groom ')
               print('5. Beautiful Bride ')
               choice=int(input('enter the choice-'))
          if choice==3:
               print('========================')
               print('8.Take marriage loan')
               print('9.Terms and conditions')
               choice=int(input('enter the choice:-'))
          if choice == 6:
               a=(input('enter the name:'))
               b=(input('enter the address:'))
               c=(input('enter the caste:'))
               d=(input('enter the appreance:'))
               e=(input('enter the age:'))
               f=(input('enter the profession:'))
               g=(input('enter the phone_no:'))
               c1=conn.cursor()
               sql_insert="insert into legends_details values( '{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g)
               c1.execute(sql_insert)
               conn.commit()
               print ('Data inserted')
               c=input('do you want to continue (y/[n]:)')
               if c =='y' :
                       continue
               else:
                         print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                         print('VISIT  AGAIN')
               
                    
          if choice==7:
               h=(input('enter the name:'))
               i=(input('enter the address:'))
               j=(input('enter the caste:'))
               k=(input('enter the appreance:'))
               l=(input('enter the age:'))
               m=(input('enter the profession:'))
               n=(input('enter the phone_no:'))
               c1=conn.cursor()
               sql_insert="insert into girls_details values( '{}','{}','{}','{}','{}','{}','{}')".format(h,i,j,k,l,m,n)
               c1.execute(sql_insert) 
               conn.commit()
               print("Details are successfully inserted")
               c=input('do you want to continue (y/[n]:)')
               if c =='y' :
                       continue
               else:
                         print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                         print('VISIT  AGAIN')
          if choice==4:
               prof=(input('Enter the profession:'))
               c1.execute("select* from legends_details where profession='{}'". format(prof))
               x = from_db_cursor(c1)
               print(x)
               c=input('do you want to continue (y/[n]:)')
               if c =='y' :
                    continue
                    
               else:
                    print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                    print('VISIT  AGAIN')
                    print()
                    break
               
          if choice==5:
               appearence=(input('Enter the appearence:'))
               c1.execute("select* from girls_details where appearence='{}'". format(appearence))
               x = from_db_cursor(c1)
               print(x)
               c=input('do you want to continue (y/[n]:)')
               if c =='y' :
                    continue
                    
               else:
                    print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                    print('VISIT  AGAIN')
                    print()
                    break
                         
          if choice==8:
               h=(input("Enter your name:"))
               j= (input("Enter the amount of loan to be taken: "))
               k= (input("Enter your bank Accountnumber: "))
               c1=conn.cursor()
               sql_insert="insert into loans values( '{}','{}','{}')".format(h,j,k)
               c1.execute(sql_insert) 
               conn.commit()
               print("The loan has been issued check your email for further updates")
               c=input('do you want to continue (y/[n]:)')
               if c =='y' :
                       continue
               else:
                         print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                         print('VISIT  AGAIN')
               
               

          if choice==9:
               print("Terms And Conditons Are:")
               print("1. You are eligible for a Personal Loan for Wedding if you are a salaried person")
               print("2. aged 21-58 years with two years of work experience")
               print("3. Our interest rates that start at 10% ")
               print("4. You should be in the present organisation for at least six months with a salary of ₹ 20,000 per month")
               print("5. Maximum Rs.20 lakh of loan can be taken")
          
