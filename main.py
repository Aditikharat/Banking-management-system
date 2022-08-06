import database as db
 
while True:
    print('''Select the operation to be performed:
    1. Open new Account
    2. Transactions
    3. Exit
    ''')
    choice = int(input('Enter Your Choice: '))
    if choice == 0:
        break
    elif choice == 1:
        name = input('Enter Your Name: ')
        acno = input('Enter Your Account no: ')
        dob = input('Enter Your DOB: ')
        address = input('Enter Your Address: ')
        phone = int(input('Enter Your Phone: '))
        ob = int(input('Enter opening balance: '))
        db.openacc(name, acno, dob, address, phone, ob)
        print('Records Inserted Successfully')
        
 
    elif choice == 2:
        print('''Select transactions :
            1. Deposit
            2. Withdraw
            3. Update customer Details
            4. Display the transactions
            5. Balance
            6. Exit
            ''')
        choice1 = int(input('Enter Your Choice: '))
        if choice1 == 1:
            db.deposite()
        elif choice1 == 2:
            db.withdraw()
        elif choice1 == 3:
            db.updaterecord()
        elif choice1 == 4:
            db.transactions()
        elif choice1 == 5:
            db.balance()
    else:
        print("Invalid case")
 