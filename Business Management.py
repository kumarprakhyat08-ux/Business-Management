import mysql.connector
from tabulate import tabulate

#For building connection
con=mysql.connector.connect(host="localhost", user='root', password='vagabondgacc')#change host, user and password accordingly
if con.is_connected()==True:
    print("Connection Established")
else:
    print("error")
c=con.cursor()

c.execute("create database if not exists Business_management;")#creates database if not exist
c.execute("use Business_management;")

c.execute("create table if not exists stocks(Stock_ID int primary key, name varchar(50), company varchar(50), price float, stock int)")#creates stocks table if not exists
c.execute("create table if not exists sales(sid int primary key, Stock_ID int, quantity float, date date, foreign key (Stock_ID) references stocks(Stock_ID))")#creates sales table if not exists


while True:
    try:    
        #for asking for login
        ID = input("\nEnter the user ID : ")
        pas = input("Enter the password : ")
        
        if ID=="manager" and pas=="man123": #for manager login
            
            while True:
                print("\nPress 1 for viewing records of stocks")
                print("Press 2 for viewing records of sales")
                print("Press 3 for adding records in stock")
                print("Press 4 for modifying records in stock")
                print("Press 5 for finding any particular record")
                print("Press 6 for exit")
                try:
                    ch1=int(input("\nEnter the choice : "))
                except Exception as e:
                    print("Error",e)
                    continue

                if ch1==1: #to show all the records stocks table
                    c.execute("select * from stocks;")
                    print(tabulate(c,headers=['Stock_ID','Name','Company','Price','Stock'],tablefmt='psql'))
                    
                
                elif ch1==2: # to show all the records from sales table
                    c.execute("select * from sales;")
                    print(tabulate(c,headers=['Sales_ID','Stock_ID','Quantity Sold','Date of selling'],tablefmt='psql'))
                    
                
                elif ch1==3: #for entry of new data in stocks table
                    try:
                        stkid=int(input("\nEnter the Stock_ID : "))
                        nam=input("Enter the name of the stock : ")
                        com=input("Enter the name of the company : ")
                        pri=float(input("Enter the price of each stock : "))
                        stk=int(input("Enter the number of stock : "))
                    
                        c.execute("insert into stocks values(%s, %s, %s, %s, %s);",(stkid, nam, com, pri, stk)) 
                        con.commit()
                        print("\nRecord inserted")

                    except Exception as e:
                        print("Error",e)
                        continue
                
                elif ch1==4: #for modifying
                    while True:
                        print("\nPress 1 for updating")
                        print("Press 2 for deleting")
                        print("Press any number to return to menu")
                        try:
                            ch2=int(input(("\nEnter choice : ")))
                        except Exception as e:
                            print("Error",e)
                            continue

                        if ch2==1: #for updating existing records of stock
                            c.execute("select Stock_ID from stocks")
                            stkid_stocks=c.fetchall()
                            c.execute('select stock from stocks')
                            stk_stocks=c.fetchall()
                            
                            for i in stkid_stocks:
                                for j in i:
                                    m_m=j
                            for i in stk_stocks:
                                for j in i:
                                    s_m=j
                            try:
                                stkid=int(input("\nEnter the Stock_ID : "))
                                nam=input("Enter the name of the stock : ")
                                com=input("Enter the name of the company : ")
                                pri=float(input("Enter the price of each stock : "))
                                stk=float(input("Enter the stock to be added : "))

                                if stkid==m_m:
                                    stk+=s_m

                                c.execute("update stocks set name=%s where Stock_ID=%s",(nam,stkid))
                                c.execute("update stocks set company=%s where Stock_ID=%s",(com,stkid))
                                c.execute("update stocks set price=%s where Stock_ID=%s",(pri,stkid))
                                c.execute("update stocks set stock=%s where Stock_ID=%s",(stk,stkid))
                                con.commit()
                                print("\nRecord updated")

                            except Exception as e:
                                print("Error",e)
                                continue

                        elif ch2==2: #for deleting the existing record
                            try:
                                stkid=int(input("\nEnter the Stock_ID : "))
                                c.execute("delete from sales where Stock_ID=%s", (stkid,))
                                c.execute("delete from stocks where Stock_ID=%s", (stkid,))
                                con.commit()
                                print("Record deleted")
                            except Exception as e:
                                print("Error",e)
                                continue
                            
                        else: #to get out of the modifying loop
                            break
                
                elif ch1==5:#For finding particular record
                    nam=input("Enter the name of the good : ")
                    c.execute("select * from stocks where Name=%s", (nam,))
                    print(tabulate(c,headers=['Stock_ID','Name','Company','Price','Stock'],tablefmt='psql'))
                    c.execute("select Stock_ID from stocks where Name=%s", (nam,))
                    s=c.fetchall()
                    for i in s:
                        for j in i:
                            stkid=j 
                    c.execute("select * from sales where Stock_ID=%s", (stkid,))
                    print(tabulate(c,headers=['Sales_ID','Stock_ID','Quantity Sold','Date of selling'],tablefmt='psql'))

                elif ch1==6: #to get out of the manager loop
                    break

                else:
                    print("Wrong choice")
                    continue

        elif ID=="salesman" and pas=="sales123": #for salesman login

            while True:
                print("\nPress 1 for viewing records of sales")
                print("Press 2 for adding records in sales")
                print("Press 3 for deleting records in sales")
                print("Press 4 for displaying any specific records from sales")
                print("Press 5 to exit")

                try:
                    s_ch1=int(input("\nEnter the choice : ")) # for entering the choice
                except Exception as e:
                    print("Error",e)
                    continue
        
                if s_ch1==1: #for showing sales table
                    c.execute("select * from sales;")
                    print(tabulate(c,headers=['Sales_ID','Stock_ID','Quantity Sold','Date of selling'],tablefmt='psql'))

                elif s_ch1==2: #for adding record in sales table
                    try:
                        sid=int(input("\nEnter the sales ID : "))
                        stkid=int(input("Enter the Stock_ID : "))
                        qty=float(input("Enter the quantity of stock sold : "))
                        date=input("Enter the date of sale (in dd-mm-yyyy format) : ")
                        
                        c.execute('select stock from stocks where Stock_ID=%s', (stkid,))
                        s=c.fetchall()
                        for i in s:
                            for j in i:
                                stk=j-qty
                        
                        #c.execute("set foreign_key_checks = 0;")
                        c.execute("insert into sales values(%s, %s, %s, str_to_date(%s, '%d-%m-%Y'))",(sid, stkid, qty, date))
                        c.execute('update stocks set stock = %s where Stock_ID=%s',(stk,stkid))
                        con.commit()
                        print("Record inserted")
                    except Exception as e:
                        print("Error",e)
                        continue

                elif s_ch1==3: #for deleting records from sales table   
                    try:
                        sid=int(input("\nEnter the sales ID : "))
                        c.execute("delete from sales where sid=%s", (sid,))
                        con.commit()
                        print("Record deleted")
                    except Exception as e:
                        print("Error",e)
                        continue

                elif s_ch1==4:#For displaying any specific record
                    sid=int(input("Enter the sales ID : "))
                    c.execute("select * from sales where sid=%s", (sid,))
                    print(tabulate(c,headers=['Sales_ID','Stock_ID','Quantity Sold','Date of selling'],tablefmt='psql'))

                elif s_ch1==5: #to get out of the sales loop
                    break

                else:
                    print("Wrong Choice")
                    continue

        else: #for wrong ID or password or to exit
            l_ch=input("Do you want to try again? (press Y for yes & any other key for no) : ")

            if l_ch=='y' or l_ch=='Y':
                pass

            else:
                break
    except Exception as e:
        print("Error",e)
        continue
