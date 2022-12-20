print("*******BANKING MANEGMENT SYSTEM*******".center(50))
    
        
def adddata_sub() :
    deposit_ini=int(input("ENTER AMT RS.5000\- TO DEPOSIT :"))#initial deposit
    if deposit_ini==5000 :
       import mysql.connector as co
    #establishing connection with mysql server
       db=co.connect(host="localhost",\
                     user="root",\
                     password="ronit",\
                     database="bank")
       cursor2=db.cursor()
       cursor2.execute("select * from information where Acc_no=(%s)", [ACC])# extracting deposit data
       data1=cursor2.fetchone()
       import pandas as pd
       import numpy as np # IN CASE DATA NEEDS TO BE MADE INTO ARRAY TO MAINTAIN SAME DTYPE
       df=pd.DataFrame(data1)# FOR FUTURE DEBUG READING VALUE TO CHECK SOURCE OF ERROR
       df[1]='ACC_NO','NAME','MOBILE_NO.','DOB','PIN','DEPOSIT','WITHDRAWN'
       print("INITIAL BANK DETAILS. . . . . . . . ".center(50))
       print('\n')
       print(df) # TEST TO MANIPULATE DATA BY CONVERTING SQL DATA TO DATFRAME OPERATING ON IT RETURNING THE MANIPULATED VALUE
       on=df.loc[(df[1] == 'DEPOSIT')] #EXTRACTING ROW
       df2=pd.DataFrame(on)#CREATING DATAFRAME OF ROW
       L1=df2.values.tolist()# CHANGING IT TO LIST FOR MATHEMATICAL OPERATION
       d1=[item[0] for item in L1]#extracted initial deposit value
       for i in d1:
           global xy
           c=abs(deposit_ini)#convert -ve value to positive 
           xy=c+i#total amt
           print('\n')
           print('PROCESSING.................'.center(50))
           print('\n')
       cursor3=db.cursor()
       updated_deposit=xy
       cursor3.execute("UPDATE information SET deposit=(%s) Where Acc_no=(%s)",[updated_deposit,ACC])
       cursor3.execute("INSERT INTO depo(Acc_no,Deposited) VALUES (%s,%s)",[ACC,c])
       cursor3.execute("INSERT INTO balance(Acc_no,t_bal) VALUES (%s,%s)",[ACC,c])
       cursor3.execute("select * from information where Acc_no=(%s)", [ACC])
       data2=cursor2.fetchone()
       df3=pd.DataFrame(data2)# FOR FUTURE DEBUG READING VALUE TO CHECK SOURCE OF ERROR
       df3[1]='ACC_NO','NAME','MOBILE_NO.','DOB','PIN','DEPOSIT','WITHDRAWN'
       print("UPDATED BANK DETAILS. . . . . . . .".center(50))
       print('\n')
       print(df3)
       print('\n')
       print("TOTAL BALANCE : RS.",xy,'\-')
       db.commit()
       cursor2.close()
       cursor3.close()
       print("*****REMEBER YOUR PIN :".center(50),PIN)
       print('\n')
       print("ACCOUNT CREATED:".center(50))
       print('\n')
       print("PRESS ENTER TO GO TO MAIN : ".center(50))
    elif deposit_ini!=5000 :
        adddata_sub()
def adddata():
    import numpy as np
    from numpy import random
    import mysql.connector as co
    #establishing connection with mysql server
    db=co.connect(host="localhost",\
              user="root",\
              password="ronit",\
              database="bank")
    name=input("ENTER NAME: ".center(50))  #inputting user name
    print('\n')
    global ACC
    ACC=random.randint(10000)#random unique acc_no given by the program
    print("ACCOUNT NO. :".center(50),ACC)#creation confirmation and acc_no display
    print('\n')
    DOB=input("ENTER DATE OF BIRTH(DD/MM/YYYY):".center(50))
    print('\n')
    global PIN
    PIN=int(input("MAKE A 4 DIGIT SECURITY PIN:".center(50)))
    print('\n')
    mob_no=input("ENTER YOUR MOBILE NO. :".center(50))
    print('\n')
    cursor=db.cursor()#creating cursor object
    insert_st="INSERT INTO information(Acc_no,Name,MOBILE_NO,DOB,PIN,Deposit,Withdrawn) VALUES (%s,%s,%s,%s,%s,0,0)"
    data=[ACC,name.upper(),mob_no,DOB,PIN]
    cursor.execute(insert_st,data)
    db.commit()
    cursor.close()
    cursor2=db.cursor()
    adddata_sub()
    x=''
    x=input()
    if (x=='') :
       menu()
       main_c()
       
def sub_exist0():
    global account
    account=int(input("ENTER ACCOUNT NO.: ".center(50)))
    sec_pin=int(input("ENTER SECURITY PIN : ".center(50)))
    import mysql.connector as co
    #establishing connection with mysql server
    db=co.connect(host="localhost",\
              user="root",\
              password="ronit",\
              database="bank")
    cursor1=db.cursor()# making 1st cursor object
    cursor1.execute("select * from information WHERE Acc_no=(%s) and PIN=(%s)",[account,sec_pin])
    data=cursor1.fetchone()
    txt="ACCOUNT_NO.\nNAME\nMOBILE_NO\nDOB\nSECURITY_PIN\nDEPOSIT\nWITDRWAN"
    seperate=txt.splitlines()
    test=(seperate,\
          data)
    for i in test:
        print('ACCOUNT_DETAILS:  ')
        print(i)
    db.commit()

def sub_exist1():
    
    print('\n')
    print("WHAT WOULD YOU LIKE TO DO :".center(50))
    print("1.DEPOSIT MONEY->".center(50))
    print("2.WITDRAW MONEY->".center(50))
    print("3.ANALYSIS ON ACCOUNT ACTIVITY->".center(50))
    print("4.CLOSE ACCOUNT->".center(50))
    print("5.EXIT->".center(50))
    

def sub_exist2() : #for deposit update
    option=int(input("ENTER OPTION : "))
    import mysql.connector as co
    #establishing connection with mysql server
    db=co.connect(host="localhost",\
              user="root",\
              password="ronit",\
              database="bank")
    if option==1 :
        deposit_amt=int(input("ENTER AMT TO DEPOSIT RS:"))
        cursor2=db.cursor()
        cursor2.execute("select * from information where Acc_no=(%s)", [account])# extracting deposit data
        data1=cursor2.fetchone()
        import pandas as pd
        import numpy as np # IN CASE DATA NEEDS TO BE MADE INTO ARRAY TO MAINTAIN SAME DTYPE
        df=pd.DataFrame(data1)# FOR FUTURE DEBUG READING VALUE TO CHECK SOURCE OF ERROR
        df[1]='ACC_NO','NAME','MOBILE_NO.','DOB','PIN','DEPOSIT','WITHDRAWN'
        print("INITIAL BANK DETAILS. . . . . . . . ".center(50))
        print('\n')
        print(df) # TEST TO MANIPULATE DATA BY CONVERTING SQL DATA TO DATFRAME OPERATING ON IT RETURNING THE MANIPULATED VALUE
        on=df.loc[(df[1] == 'DEPOSIT')] #EXTRACTING ROW
        df2=pd.DataFrame(on)#CREATING DATAFRAME OF ROW
        L1=df2.values.tolist()# CHANGING IT TO LIST FOR MATHEMATICAL OPERATION
        d1=[item[0] for item in L1]#extracted initial deposit value
        for i in d1:
           global xy
           c=abs(deposit_amt)#convert -ve value to positive 
           xy=c+i#total amt
           print('\n')
           print('PROCESSING.................'.center(50))
           print('\n')
        cursor3=db.cursor()
        updated_deposit=xy###############################################################################################
        cursor3.execute("UPDATE information SET deposit=(%s) Where Acc_no=(%s)",[updated_deposit,account])
        cursor3.execute("INSERT INTO depo(Acc_no,Deposited) VALUES (%s,%s)",[account,c])
        cursor3.execute("INSERT INTO balance(Acc_no,t_bal) VALUES (%s,%s)",[account,xy])
        cursor3.execute("select * from information where Acc_no=(%s)", [account])
        data2=cursor2.fetchone()
        df3=pd.DataFrame(data2)# FOR FUTURE DEBUG READING VALUE TO CHECK SOURCE OF ERROR
        df3[1]='ACC_NO','NAME','MOBILE_NO.','DOB','PIN','DEPOSIT','WITHDRAWN'
        print("UPDATED BANK DETAILS. . . . . . . .".center(50))
        print('\n')
        print(df3)
        print('\n')
        print("TOTAL BALANCE : RS.",xy,'\-')
        db.commit()
        cursor3.close()
        print("PRESS ENTER TO EXIT: ".center(50))
        x=''
        x=input()
        if (x=='') :
           menu()
           main_c()
           
    elif option== 2 :
        withdraw_amt=int(input("ENTER AMT TO WITHDRAW RS:"))
        cursor2=db.cursor()
        cursor2.execute("select * from information where Acc_no=(%s)", [account])# extracting deposit data
        data1=cursor2.fetchone()
        import pandas as pd
        import numpy as np # IN CASE DATA NEEDS TO BE MADE INTO ARRAY TO MAINTAIN SAME DTYPE
        df=pd.DataFrame(data1)# FOR FUTURE DEBUG READING VALUE TO CHECK SOURCE OF ERROR
        df[1]='ACC_NO','NAME','MOBILE_NO.','DOB','PIN','DEPOSIT','WITHDRAWN'
        print("INITIAL BANK DETAILS. . . . . . . . ".center(50))
        print('\n')
        print(df) # TEST TO MANIPULATE DATA BY CONVERTING SQL DATA TO DATFRAME OPERATING ON IT RETURNING THE MANIPULATED VALUE
        
        cursor4=db.cursor()
        cursor4.execute("select * from information where Acc_no=(%s)", [account])# extracting deposit data
        data2=cursor4.fetchone()
        df4=pd.DataFrame(data2)# FOR FUTURE DEBUG READING VALUE TO CHECK SOURCE OF ERROR
        df4[1]='ACC_NO','NAME','MOBILE_NO.','DOB','PIN','DEPOSIT','WITHDRAWN'
        print("INITIAL BANK DETAILS. . . . . . . . ".center(50))
        print('\n')
        on1=df4.loc[(df[1] == 'DEPOSIT')] #EXTRACTING ROW
        df5=pd.DataFrame(on1)#CREATING DATAFRAME OF ROW
        L2=df5.values.tolist()# CHANGING IT TO LIST FOR MATHEMATICAL OPERATION
        d2=[item[0] for item in L2]#extracted initial deposit value
        for b in d2:
           if b>5000 and b-withdraw_amt>=5000 :
              on=df.loc[(df[1] == 'WITHDRAWN')] #EXTRACTING ROW
              df2=pd.DataFrame(on)#CREATING DATAFRAME OF ROW
              L1=df2.values.tolist()# CHANGING IT TO LIST FOR MATHEMATICAL OPERATION
              d1=[item[0] for item in L1]#extracted initial withdrawn value
              for i in d1:
                 global yz
                 c=abs(withdraw_amt)#keep the value positive 
                 yz=b-c#updated balance
                 print('\n')
                 print('PROCESSING.................'.center(50))
                 print('\n')
              cursor3=db.cursor()
              updated_bal=yz
              cursor3.execute("UPDATE information SET deposit=(%s) Where Acc_no=(%s)",[updated_bal,account])
              cursor3.execute("UPDATE information SET WITHDRAWN=(%s) Where Acc_no=(%s)",[c,account])
              cursor3.execute("INSERT INTO withdraw(Acc_no,withdrwan) VALUES (%s,%s)",[account,c])
              cursor3.execute("INSERT INTO balance(Acc_no,t_bal) VALUES (%s,%s)",[account,yz])
              cursor3.execute("select * from information where Acc_no=(%s)", [account])
              data2=cursor2.fetchone()
              df3=pd.DataFrame(data2)# FOR FUTURE DEBUG READING VALUE TO CHECK SOURCE OF ERROR
              df3[1]='ACC_NO','NAME','MOBILE_NO.','DOB','PIN','DEPOSIT','WITHDRAWN'
              print("UPDATED BANK DETAILS. . . . . . . .".center(50))
              print('\n')
              print(df3)
              print('\n')
              print("TOTAL withdrawn : RS.",c,'\-')
              cursor3.execute("UPDATE information SET WITHDRAWN=0 Where Acc_no=(%s)",[account])
              
              db.commit()
              cursor3.close()
              print("PRESS ENTER TO EXIT: ".center(50))
              x=''
              x=input()
              if (x=='') :
                 menu()
                 main_c()
                 
           else :
              print("INSUFFICIENT BALANCE...........".center(50))
              print("PRESS ENTER TO EXIT: ".center(50))
              x=''
              x=input()
              if (x=='') :
                 menu()
                 main_c()
    elif option==3:
        cursor5=db.cursor()
        cursor5.execute("select * from depo having Acc_no=(%s)", [account])# extracting deposit data
        data3=cursor5.fetchall()
        cursor5.execute("select * from withdraw having Acc_no=(%s)", [account])# extracting withdraw data data
        data4=cursor5.fetchall()
        cursor5.execute("select * from balance having Acc_no=(%s)", [account])# extracting total balance data
        data5=cursor5.fetchall()
        import pandas as pd
        import matplotlib.pyplot as plt
        df=pd.DataFrame(data5)
        df1=pd.DataFrame(data3)
        df2=pd.DataFrame(data4)
        df.columns=['sno','account_no','balance']
        df1.columns=['sno','account_no','deposit']
        df2.columns=['sno','account_no','withdrawn']
        axis = plt.subplots(1, 3)
        ax=df.reset_index().plot(x='index',y='balance',grid=True,title='ACCOUNT_ANALYSIS')
        df1.reset_index().plot(x='index',y='deposit',grid=True,title='ACCOUNT_ANALYSIS',ax=ax)
        df2.reset_index().plot(x='index',y='withdrawn',grid=True,title='ACCOUNT_ANALYSIS',ax=ax)
        ax.set_xlabel("INDEX")
        ax.set_ylabel('AMT(in RS.)')
        plt.show()
        print("PRESS ENTER TO EXIT: ".center(50))
        x=''
        x=input()
        if (x=='') :
            menu()
            main_c()
        
        
        
    elif option==4:
        print("ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT: ".center(50))
        print("PRESS ENTER TO CONTINUE>>")
        print("TO DISCONTINUE PRESS 'N'")
        x=input()
        if (x=='') :
            cursor4=db.cursor()
            cursor4.execute("delete from depo where Acc_no=(%s)", [account])
            cursor4.execute("delete from withdraw where Acc_no=(%s)", [account])
            cursor4.execute("delete from balance where Acc_no=(%s)", [account])
            cursor4.execute("delete from information where Acc_no=(%s)", [account])
            db.commit()
            cursor4.close()
            print("ACCOUNT DELETED SUCCESFULLY.......................".center(50))
            print("\n")
            menu()
            main_c()
        elif(x=='n' or x=='N'):
            menu()
            main_c()
    elif option==5:
        print("PRESS ENTER TO EXIT: ".center(50))
        x=''
        x=input()
        if (x=='') :
           menu()
           main_c()
def admin():
    import mysql.connector as co
    #establishing connection with mysql server
    db=co.connect(host="localhost",\
                  user="root",\
                  password="ronit",\
                  database="bank")
    cursor5=db.cursor()
    print("ALL ACCOUNT INFORMATION:>>>>>>>>>>>")
    cursor5.execute("select * from information ")
    data6=cursor5.fetchall()
    for i in data6 :
       print(i)
    print('\n')
    print("ALL DEPOSITS INFORMATION:>>>>>>>>>>>>>")
    cursor5.execute("select * from depo ")
    data3=cursor5.fetchall()
    for i in data3 :
       print(i)
    print('\n')
    print("ALL WITDRAWN INFORMATION:>>>>>>>>>>>")
    cursor5.execute("select * from withdraw ")
    data4=cursor5.fetchall()
    for i in data4 :
       print(i)
    print('\n')
    print("ALL BALANCE INFORMATION:>>>>>>>>>>>")
    cursor5.execute("select * from balance ")
    data5=cursor5.fetchall()
    for i in data5 :
       print(i)
    print('\n')
    cursor5.close()
    print("restart !!!!!!!!!!!")
   
def exist():
    sub_exist0()
    sub_exist1()
    sub_exist2()
    

          
def main_c() :
   choice=int(input("ENTER YOUR CHOICE :  "))# choose the option provided by menu()
   if choice==1 :
      adddata()
   elif choice==2 :
      exist()
   elif choice==3 :
      global admin_pin
      admin_pin=12098
      print ("ENTER ADMIN PIN : ".center(50))
      global ap
      ap=int(input())
      if ap==admin_pin:
          admin()
      else :
          main_c()
   elif choice==4 or choice>=3 :
      print("EXITING.....")
      


def menu():
    x=''
    if (x==''):
        print(":...WELCOME...: ".center(50))
        print("1. NEW ACCOUNT".center(50))
        print("2. EXISTING ACCOUNT".center(50))
        print("3. FOR ADMIN".center(50))
        print("4. EXIT".center(50))

        
def intro():   
    x=input("PRESS ENTER TO START:  ") # start of programme
    menu()
    main_c()

intro()   

    
    
   
   
    
    
    
    
