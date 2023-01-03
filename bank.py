import mysql.connector as a
mydb = a.connect(host='localhost', user='root', password='', database='bank_management')

def OpenAcc():
    n = input('Enter the Name: ')
    ac = input('Enter the Account Number: ')
    db = input('Enter the Date of Birth: ')
    add = input('Enter the Address: ')
    cn = input('Enter the Contact Number: ')
    ob = int(input('Enter the Opening Balance: '))
    data1 = (n, ac, db, add, cn, ob)
    data2 = (n, ac, ob)
    sql1 = ('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into amount values(%s,%s,%s)')
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print('Data Entered Successfully')
    main()

def depositAmount():
    amount= int(input('Enter the amount you want to deposit: '))
    ac = input('Enter the Account Number: ')
    a = 'select balance from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] + amount
    sql = 'update amount set balance=%s where AccNo=%s'
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()

def withdrawAmount():
    amount = int(input('Enter the amount you want to withdraw: '))
    ac = input('Enter the Account Number: ')
    a = 'select balance from amount where  AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = 'update amount set balance=%s where AccNo=%s'
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()

def balanceEnq():
    ac = input("Enter the account no: ")
    a = 'select balance from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    print('Balance for account: ', ac, 'is', result[0])
    main()

def displayDetails():
    ac = input("Enter the account no: ")
    a = 'select * from account where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i,end=" ")
    main()

def CloseAcc():
    ac = input("Enter the account no: ")
    sql1 = 'delete from account where AccNo=%s'
    sql2 = 'delete from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(sql1, data)
    x.execute(sql2, data)
    mydb.commit()
    main()




def main():
    print('''
                  1.OPEN NEW ACCOUNT
                  2.DEPOSIT AMOUNT
                  3.WITHDRAW AMOUNT
                  4.BALANCE ENQUIRY
                  5.DISPLAY CUSTOMER DETAILS
                  6.CLOSE ACCOUNT''')
    choice = input('Enter the Task you want to perform:')
    if (choice =='1'):
        OpenAcc()
    elif (choice =='2'):
        depositAmount()
    elif (choice =='3'):
        withdrawAmount()
    elif (choice =='4'):
        balanceEnq()
    elif (choice =='5'):
        displayDetails()
    elif (choice =='6'):
        CloseAcc()
    else:
        print('Invalid')
        main()
main()

