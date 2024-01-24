import mysql.connector as mys
database=mys.connect(host="localhost",user="root",passwd="nik@MYSQL#11",database="data_management_in_construction_industry")
p=database.cursor()
if database.is_connected():
    print("                         CONSTRUCTION INDUSTRY DATABASE                         ")                    
    wait=input("\n\npress 'ENTER' to set up a new database(press ANY KEY if it already exists)")
    if wait=='':
        p.execute("create database data_management_in_construction_industry")
        database.commit()
        p.execute("use data_management_in_construction_industry")
        database.commit()
        def adminlogin():
            p.execute("create table adminlogin(username varchar(20),passwd varchar(20))")
            database.commit()
            usr='andrew'
            passwd='TASM3'
            p.execute("insert into adminlogin values('%s','%s')"%(usr,passwd))
            database.commit()
        def userlogin():
            p.execute("create table userlogin(id int NOT NULL PRIMARY KEY,name varchar(20),passwd varchar(20))")
            database.commit()
        def ConstructionDataTable():
            p.execute("create table constructioninfo(customer_ID int NOT NULL PRIMARY KEY,customer_name varchar(20),type_of_construction varchar(20),area int,location varchar(20),date_of_completion date, status varchar(20))")
            database.commit()
        def ConstructionAspects():
            p.execute("create table constructionaspects(customer_ID int NOT NULL PRIMARY KEY, project varchar(30), no_of_workers int,cost_of_raw_materials int,labour_charges int)")
            database.commit()
        adminlogin()
        userlogin()
        ConstructionDataTable()
        ConstructionAspects()
        
def insertadminloginvalues():
    n=int(input("enter the no. of people you need to assign"))
    for i in range(n):
        a=input("Username: ")
        b=input("Password: ")
        p.execute("insert into adminlogin values('%s','%s')"%(a,b))
        database.commit()
    print("Saved successfully")
        
def insertuserloginvalues():
    n=int(input("Enter the number of users to be registered"))
    for i in range(n):
        a=int(input("Enter the ID : "))
        b=input("Name : ")
        c=input("Password : ")
        p.execute("insert into userlogin values(%s,'%s','%s')"%(a,b,c))
        database.commit()
    print("Saved successfully")
    
def insertConstructionData():
    a=int(input("Customer ID : "))
    b=input("Customer Name : ")
    c=input("Structure to be constructed : ")
    d=int(input("Area (in sq.feet) : "))
    e=input("Location of construction : ")
    f=input("Date of completion : ")
    g=input("Status of construction : ")
    p.execute("insert into constructioninfo values('%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g))
    p.execute("insert into constructionaspects(customer_ID,project) values('%s','%s')"%(a,c))
    database.commit()
    h = input("Do you wish to continue with the entered data ? (Y/N) : ")
    while h in ('n','no','No','N','NO'):
        break
    while h in ('y','yes','Yes','Y','YES'):
        print("Data saved successfully")
        break
        
            
    
def changestatus():
    a=int(input("Enter the customer ID  : "))
    p.execute("select * from constructioninfo where customer_ID=%s"%(a))
    b = p.fetchall()
    rows = p.rowcount
    for i in b:
        newstatus = input("Enter the updated status : ")
        p.execute("UPDATE constructioninfo SET status='%s' where customer_ID=%s"%(newstatus,a))
        print("The status of construction has been updated")
        database.commit()
    if rows!=1:
        print("Invalid Customer ID")
        print("\n")  
        
def changedeets():
    credential=int(input('''In which field would you like to add/change data ?
            \n1.No. of workers
2.Cost of raw materials
3.Labour charges
4.Previous Menu
\nEnter your choice : '''))
    if credential==1:
        a =int(input("Enter the customer ID : "))
        p.execute("select * from constructionaspects where customer_ID=%s"%(a))
        b=p.fetchall()
        rows=p.rowcount
        for i in b:
            number=int(input("Enter the no. of workers: "))
            p.execute("UPDATE constructionaspects SET no_of_workers='%s' where customer_ID=%s"%(number,a))
            database.commit()
            print("The number of workers has been updated")
        if rows!=1:
            print("Invalid Customer ID")
            print("\n")
    if credential==2:
        x=int(input("Enter the customer ID : "))
        p.execute("select * from constructionaspects where customer_ID=%s"%(x))
        b=p.fetchall()
        rows=p.rowcount
        for i in b:
            cost=int(input("Enter the cost of raw materials: "))
            p.execute("UPDATE constructionaspects SET cost_of_raw_materials='%s' where customer_ID=%s"%(cost,x))
            database.commit()
            print("The cost of raw materials has been updated")
        if rows!=1:
            print("Invalid Customer ID")
            print("\n")
    if credential==3:
        y=int(input("Enter the customer ID : "))
        p.execute("select * from constructionaspects where customer_ID=%s"%(y))
        b=p.fetchall()
        rows=p.rowcount
        for i in b:
            labourcharges=int(input("Enter the cost of labour: "))
            p.execute("UPDATE constructionaspects SET labour_charges='%s' where customer_ID=%s"%(labourcharges,y))
            database.commit()
            print("The labour charges have been updated")
        if rows!=1:
            print("Invalid Customer ID")
            print("\n")
    if credential==4:
        adminfunction=int(input('''Choose the operation you would like to perform
                    \n1.Enter new admin record
2.Enter new customer credentials
3.Alter allotted construction details
4.Search using user entries
5.Search using allotted records
6.Exit
\nEnter your choice : '''))
        if adminfunction==1:
            insertadminloginvalues()
        if adminfunction==2:
            insertuserloginvalues()
        if adminfunction==3:
            changedeets()
        if adminfunction==4:
            search()
        if adminfunction==5:
            search2()
        while adminfunction==6:
            break
            
def user():
    a=int(input("Enter the customer ID : "))
    p.execute("select * from constructioninfo where customer_ID=%s"%(a))
    b=p.fetchall()
    rows=p.rowcount
    for i in b:
        print(i)
        print()
        print("The status of your construction is : ",b[0][6])
    if rows!=1:
        print("Invalid customer ID")
        print("\n")
        
def details():
    count=0
    statusofcons=input("Enter the status of construction : ")
    location=input("Enter the location : ")
    p.execute("select * from constructioninfo where status='%s' and location='%s'"%(statusofcons,location))
    b=p.fetchall()
    rows=p.rowcount
    for i in b:
        count+=1
    print("There are",count,statusofcons,"constructions in",location)
    condition=input("Do you want to view the details ? (Y/N) : ")
    if condition in ('y','Y','yes','Yes','YES'):
        print(i)
        
def search():
    searching=int(input('''Enter the field you would like to search by
            \n1. Structure of construction
2. Location
3. Year
4. Previous Menu
\nEnter your choice : '''))
    if searching==1:
        struc=input("Enter the structure : ")
        p.execute("select * from constructioninfo where type_of_construction='%s'"%(struc))
        b=p.fetchall()
        rows=p.rowcount
        if rows==0:
            print("There are no records for the given structure")
        else:
            for i in b:
                print(b)
                print('='*55)
    if searching==2:
        loca=input("Enter the location : ")
        p.execute("select * from constructioninfo where location='%s'"%(loca))
        b=p.fetchall()
        rows=p.rowcount
        if rows==0:
            print("There are no records for the given location")
        else:
            for i in b:
                print(b)
                print('='*55)
    if searching==3:
        year=input("Enter the year : ")
        yr = int(input('''Choose the status of records you would like to see :
                \n1. Completed
2. Pending
3. Previous Menu
                \nEnter your choice : '''))
        if yr==1:
            p.execute("select * from constructioninfo where year(date_of_completion)='%s' and status='completed'"%(year))
            b=p.fetchall()
            rows=p.rowcount
            if rows==0:
                print("There are no completed constructions in the given year")
            else:
                for i in b:
                    print(i)
                    print('='*60)
        if yr==2:
            p.execute("select * from constructioninfo where year(date_of_completion)='%s' and status='%s'"%(year,"pending"))
            b=p.fetchall()
            rows=p.rowcount
            if rows==0:
                print("There are no pending constructions in the given year")
            else:
                for i in b:
                    print(i)
                    print('='*60)
        if yr==3:
            search()
    if searching==4:
        adminfunction=int(input('''Choose the operation you would like to perform
                    \n1.Enter new admin record
2.Enter new customer credentials
3.Alter allotted construction details
4.Search using user entries
5.Search using allotted records
6.Exit
\nEnter your choice : '''))
        if adminfunction==1:
            insertadminloginvalues()
        if adminfunction==2:
            insertuserloginvalues()
        if adminfunction==3:
            changedeets()
        if adminfunction==4:
            search()
        if adminfunction==5:
            search2()
        while adminfunction==6:
            break
            
def search2():
    searching2=int(input('''Enter the field whose details you would like to see
            \n1. No. of workers
2. Cost of raw materials
3. Cost of labour
4. Previous Menu
\nEnter your choice : '''))
    if searching2==1:
        work=int(input("Enter the customer ID : "))
        p.execute("select customer_ID,project,no_of_workers from constructionaspects where customer_ID=%s "%(work))
        b=p.fetchall()
        rows=p.rowcount
        if rows==0:
            print("No workers have been assigned for the given task")
        else:
            for i in b:
                print(i)
                print('='*60)
    if searching2==2:
        costofrm=int(input("Enter the customer ID : "))
        p.execute("select customer_ID,project,cost_of_raw_materials from constructionaspects where customer_ID=%s "%(costofrm))
        b=p.fetchall()
        rows=p.rowcount
        if rows==0:
            print("The cost has not been assigned for the given project")
        else:
            for i in b:
                print(i)
                print('='*60)
    if searching2==3:
        laborcost=int(input("Enter the customer ID : "))
        p.execute("select customer_ID,project,labour_charges from constructionaspects where customer_ID=%s "%(laborcost))
        b=p.fetchall()
        rows=p.rowcount
        if rows==0:
            print("The labour charges have not been assigned for the given project")
        else:
            for i in b:
                print(i)
                print('='*60)
    if searching2==4:
        adminfunction=int(input('''Choose the operation you would like to perform
                    \n1.Enter new admin record
2.Enter new customer credentials
3.Alter allotted construction details
4.Search using user entries
5.Search using allotted records
6.Exit
\nEnter your choice : '''))
        if adminfunction==1:
            insertadminloginvalues()
        if adminfunction==2:
            insertuserloginvalues()
        if adminfunction==3:
            changedeets()
        if adminfunction==4:
            search()
        if adminfunction==5:
            search2()
        while adminfunction==6:
            break
                
def adminchoice():
    uname=input("Enter the username: ")
    upass=input("Enter the password: ")
    p.execute("select * from adminlogin where username='%s' and passwd='%s'"%(uname,upass))
    p.fetchall()
    rows=p.rowcount
    if rows!=1:
        print("Incorrect login details")
    else:
        print("Welcome",uname,"!")
        print('\n')
        while True:
            adminfunction=int(input('''Choose the operation you would like to perform
                    \n1.Enter new admin record
2.Enter new customer credentials
3.Alter allotted construction details
4.Search using user entries
5.Search using allotted records
6.Main Menu
\nEnter your choice : '''))
            if adminfunction==1:
                insertadminloginvalues()
            if adminfunction==2:
                insertuserloginvalues()
            if adminfunction==3:
                changedeets()
            if adminfunction==4:
                search()
            if adminfunction==5:
                search2()
            if adminfunction==6:
                break
            
def contractorchoice():
    uname=input("Enter the username: ")
    upass=input("Enter the password: ")
    p.execute("select * from adminlogin where username='%s' and passwd='%s'"%(uname,upass))
    p.fetchall()
    rows=p.rowcount
    if rows!=1:
        print("Incorrect login details")
    else:
        print("Welcome",uname,"!")
        print('\n')
        while True:
            adminfunction=int(input('''Choose the operation you would like to perform
                    \n1.Enter new construction record
2.Change the status of construction projects
3.Annual report
4.Main Menu
\nEnter your choice : '''))
            if adminfunction==1:
                insertConstructionData()
            if adminfunction==2:
                changestatus()
            if adminfunction==3:
                custom=int(input("Enter the customer ID : "))
                report=input("Enter the year: ")
                p.execute("select count(customer_ID) from constructioninfo where year(date_of_completion)=%s"%(report))
                b=p.fetchall()
                rows=p.rowcount
                if rows==0:
                    print("No records found")
                else:
                    for i in b:
                        for j in i:
                            print(j,"construction(s) took place in the year",report)
                            k=input("Do you wish to see the details of the records ? (Y/N): ")
                            if k in ('y','Y','yes','Yes','YES'):
                                p.execute("select * from constructioninfo where year(date_of_completion)=%s"%(report))
                                b=p.fetchall()
                                rows=p.rowcount
                                if rows==0:
                                    print("No records found")
                                else:
                                    for i in b:
                                        print(i,end='\n')
                                        print('='*120)
                            l=input("Do you wish to see the no. of workers and costs ? (Y/N): ")
                            if l in ('y','Y','yes','Yes','YES'):
                                p.execute("select no_of_workers,cost_of_raw_materials,labour_charges from constructionaspects where customer_ID=%s"%(custom))
                                a=p.fetchall()
                                rows=p.rowcount
                                if rows==0:
                                    print("No records found")
                                else:
                                    for x in a:
                                        print(x,end='\n')
                                        print('='*120)
            if adminfunction==4:
                break
            
def userchoice():
    uname=input("Enter your name: ")
    upass=input("Enter your password: ")
    p.execute("select * from userlogin where name='%s' and passwd='%s'"%(uname,upass))
    p.fetchall()
    rows=p.rowcount
    if rows!= 1:
        print("Incorrect user credentials")
        choice()
    else:
        print("Welcome",uname,"!")
        print('\n')
        user()
        print("="*120)
        print('\n')
         
while True:
    print('\n')
    print(" CONSTRUCTION SERVICES AND RECORDS ")
    print('-'*100)
    choice=int(input('''\n1. Admin login
2. Contractor login
3. View construction status
4. Exit database
\nEnter your choice : '''))
    if choice==1:
        adminchoice()
    if choice==2:
        contractorchoice()
    if choice==3:
        userchoice()
    if choice==4:
        break

            
                    
                   
                
                 
                
        
            
            
             
                 
                  
          
     
            
       
       
      
      
      
      

          
     
        

