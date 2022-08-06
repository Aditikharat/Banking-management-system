import pymysql

 
con = pymysql.connect(host='localhost',
                        database='banksystem',
                        user='root',
                        password='root')
cur=con.cursor()
 
def openacc(name,acno,dob,address,phone,ob):
    query = f'insert into act(name,acno,dob,address,phone,balance) values ("{name}","{acno}","{dob}","{address}",{phone},{ob})'
    cur.execute(query)
    query = f'insert into amt(acno,current_balance,previous_balance,Transaction_type) values (%s,%s,%s,%s)'
    cur.execute(query, [acno, ob, ob, 'Credited'])
    con.commit()
    con.commit()
 
 
def updaterecord():
    global column, newvalue, query
    acno = input('Enter the account number of customer whose records is to be updated: ')
 
    print('''What do you want to update?
                1. name
                2. dob
                3. address
                4. phone
            ''')
    updatechoice = int(input('Enter Your Choice: '))
 
    if updatechoice == 1:
        newvalue = input('Enter New Name: ')
        column = 'name'
        query = f'update act set name = "{newvalue}" where acno = {acno}'
    elif updatechoice == 2:
        newvalue = input('Enter New date of birth: ')
        column = 'dob'
        query = f'update act set {column} = "{newvalue}" where acno = {acno}'
    elif updatechoice == 3:
        newvalue = input('Enter New Address: ')
        column = 'address'
        query = f'update act set {column} = "{newvalue}" where acno = {acno}'
    elif updatechoice == 4:
        newvalue = int(input('Enter New Phone: '))
        column = 'phone'
        query = f'update act set {column} = "{newvalue}" where acno = {acno}'
 
    cur.execute(query)
    con.commit()
    print("Updated successfully")
 
 
def balance():
    acno = input("Enter account number: ")
    query=f'select balance from act where acno=%s'
    c = con.cursor()
    c.execute(query, [acno])
    myresult = c.fetchone()
    print(myresult[0])
 
def transactions():
    acno = input("Enter account number: ")
    query = f'select * from amt where acno=%s'
    c = con.cursor()
    c.execute(query, [acno])
    myresult = c.fetchall()
    print(myresult)
    con.commit()
 
def deposite():
    amt = int(input("Enter amount:"))
    acno = input("Enter account number: ")
    a = "select balance from act where acno=%s"
    c = con.cursor()
    c.execute(a, [acno])
    myresult = c.fetchone()
    print(myresult[0])
    tam = int(myresult[0]) + int(amt)
    sql1 = "update act set balance=%s where acno=%s"
    c.execute(sql1, [tam,acno])
    query = f'insert into amt(acno,current_balance,previous_balance,Transaction_type) values (%s,%s,%s,%s)'
    cur.execute(query, [acno, tam, myresult[0], 'Credited'])
    con.commit()
    print(f'Credited {amt} in {acno} account')
 
 
class minbalance(Exception):
    pass
 
def withdraw():
    amt = int(input("Enter amount:"))
    acno = input("Enter account number: ")
    cur = con.cursor()
    a = "select balance from act where acno=%s"
    c = con.cursor()
    c.execute(a, [acno])
    myresult = c.fetchone()
    print(myresult[0])
    tam = int(myresult[0]) - int(amt)
    try:
        if tam<=5000:
            raise minbalance
        else:
            sql1 = "update act set balance=%s where acno=%s"
            c.execute(sql1, [tam, acno])
            query = f'insert into amt(acno,current_balance,previous_balance,Transaction_type) values (%s,%s,%s,%s)'
            cur.execute(query, [acno, tam, myresult[0], 'Deducted'])
            con.commit()
            print(f'Deducted {amt} in {acno} account')
    except minbalance:
        print("Sorry, The minimum balance to be maintained is 5000.")
 
