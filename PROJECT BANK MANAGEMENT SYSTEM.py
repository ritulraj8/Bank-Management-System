# PROJECT BANK MANAGEMENT SYSTEM
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",
                               passwd="1234", database="bankdb")
mycursor = mydb.cursor()


def menu():  # Function to display the menu
    print("*" * 150)
    print("Main Menu".center(150))
    print("1. Insert Record/Records".center(150))
    print("    a. Sort as per Account Number".center(150))
    print("    b. Sort as per Customer Name".center(150))
    print("    c. Sort as per Customer Balance ".center(150))
    print("3. Search Record details as per account number".center(150))
    print("4. Update Record".center(150))
    print("5. Delete Record".center(150))
    print("6. Transactions Debit/Credit from/into Account".center(150))
    print("     a. Debit/Withdraw from Account".center(150))
    print("     b. Credit into the Account".center(150))
    print("7. Exit".center(150))
    print("*" * 150)


def menusort():
    print("    a. Sort as per Account Number".center(150))
    print("    b. Sort as per Customer Name".center(150))
    print("    c. Sort as per Customer Balance ".center(150))
    print("   d. Back".center(150))


def menutransaction():
    print("     a. Debit/Withdraw from Account".center(150))
    print("     b. Credit into the Account".center(150))
    print("     c. Back".center(150))


def Create():  # Function to create table
    try:
        com = "create table Bank(ACCNO varchar(20) primary key,NAME varchar(20) NOT NULL,MOBILE varchar(20) NOT NULL,EMAIL varchar(20) NOT NULL,ADDRESS varchar(20) NOT NULL,CITY varchar(20) NOT NULL,COUNTRY varchar(20) NOT NULL,BALANCE DECIMAL(12,2) NOT NULL)"
        mycursor.execute(com)
        print("Table Created")
    except:
        print("Insert data")
        insert()


def insert():
    while True:  # Loop for accepting records1
        acc = input("Enter Account Number ")
        name = input("Enter Name ")
        mob = input("Enter Mobile Number ")
        email = input("Enter Email address ")
        address = input("Enter Address ")
        city = input("Enter City ")
        country = input("Enter Country ")
        Balance = float(input("Enter Balance amount "))
        cmd = "insert into bank values('{}','{}',{},'{}','{}','{}','{}',{})".format(acc,name.upper(),mob,email.upper(),address.upper(),city.upper(),country.upper(),Balance)
        mycursor.execute(cmd)
        mydb.commit()  # This method is used to make sure the changes are consistent
        ch = input("Do you want to add more records? (Y/N) ")# asking the user if they want to add more records
        if ch in ["y","Y"]:
            insert()
        elif ch in ["n", "N"]:
            break
        else:
            print("Invalid choice")
            break
def dispsortacc():  # Function to display records as per ascending order of Account Number
    try:
        com = "select * from bank order by accno"
        mycursor.execute(com)  # Function to execute the command in mysql
        dat = mycursor.fetchall()  # This function retrieves all rows of a query result
        f = "%15s %15s %15s %15s %15s %15s %15s %15s "  # %15s here is used to seperate each attribute by 15 spaces
        print(f % ("accno", "name", "mobile", "email", "address", "city", "country", "balance"))
        print("=" * 125)
        for i in dat:  # For traversing through the list of records
            for j in i:  # For traversing through each record
                print("%16s" % j, end="")
            print()
            print("=" * 125)
    except:
        print("Table doesn't exist")





def dispsortname():  # Function to display records as per ascending order of Customer Name
    try:
        com = "select * from bank order by name"
        mycursor.execute(com)  # Function to execute the command in mysql
        dat = mycursor.fetchall()  # This function retrieves all rows of a query result
        f = "%15s %15s %15s %15s %15s %15s %15s %15s "
        print(f % ("accno", "name", "mobile", "email", "address", "city", "country", "balance"))
        print("=" * 125)
        for i in dat:  # For traversing through the list of records
            for j in i:  # For traversing through each record
                print("%16s" % j, end="")
            print()
            print("=" * 125)
    except:
        print("Table doesn't exist")


def dispsortBal():  # Function to display records as per ascending order of Account Balance
    try:
        com = "select * from bank order by balance"
        mycursor.execute(com)  # Function to execute the command in mysql
        dat = mycursor.fetchall()  # This function retrieves all rows of a query result
        f = "%15s %15s %15s %15s %15s %15s %15s %15s "
        print(f % ("accno", "name", "mobile", "email", "address", "city", "country", "balance"))
        print("=" * 125)
        for i in dat:  # For traversing through the list of records
            for j in i:  # For traversing through each record
                print("%16s" % j, end="")
            print()
            print("=" * 125)
    except:
        print("Table doesn't exist")


def dispsearchacc():  # Function to search for the record from the file with respect to Account Number
    try:
        com = "select * from bank"
        mycursor.execute(com)  # Function to execute the command in mysql
        s = mycursor.fetchall()  # This function retrieves all rows of a query result
        ch = input("Enter Account number to be searched ")
        for i in s:  # For traversing through the list of records
            if i[0] == ch:  # The first element of each record is the Account Number.
                print("=" * 125)
                f = "%15s %15s %15s %15s %15s %15s %15s %15s "
                print(f % ("accno", "name", "mobile", "email", "address", "city", "country", "balance"))
                print("=" * 125)
                for j in i:  # For traversing through each record
                    print("%16s" % j, end="")
                print()
                break  # To end the loop after finding the required Account Number
        else:  # If the Condition is not fulfilled ,for that purpose we ll use else statement
            print("Record not found")
    except:
        print("Table doesn't exist")


def update():  # Function to change the details of a customer
    try:
        com = "select * from bank"
        mycursor.execute(com)  # Function to execute the command in mysql
        s = mycursor.fetchall()  # This function retrieves all rows of a query result
        a = input("Enter the Account Number whose details are to be changed ")
        for i in s:  # For traversing through the list of record
            l = list(i)
            if l[0] == a:  # The first element of each record is the Account Number.
                ch = input("Change Name (Y/N)? ")
                if ch in ["y", "Y"]:
                    l[1] = input("Enter name ")
                    l[1] = l[1].upper()
                ch = input("Change Mobile (Y/N)? ")
                if ch in ["y", "Y"]:
                    l[2] = input("Enter Mobile Number ")
                ch = input("Change Email (Y/N)? ")
                if ch in ["y", "Y"]:
                    l[3] = input("Enter Email ")
                    l[3] = l[3].upper()
                ch = input("Change Address (Y/N)? ")
                if ch in ["y", "Y"]:
                    l[4] = input("Enter Address ")
                    l[4] = l[4].upper()
                ch = input("Change City (Y/N)? ")
                if ch in ["y", "Y"]:
                    l[5] = input("Enter City ")
                    l[5] = l[5].upper()
                ch = input("Change Country (Y/N)? ")
                if ch in ["y", "Y"]:
                    l[6] = input("Enter Country ")
                    l[6] = l[6].upper()
                ch = input("Change Balance (Y/N)? ")
                if ch in ["y", "Y"]:
                    l[7] = input("Enter Balance ")

                com = "UPDATE bank set NAME=%s,Mobile=%s,email=%s,address=%s,city=%s,country=%s,balance=%s where accno=%s"  # MYSQL command to update the records
                val = (l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[0],)  # Each %s corresponds to each attribute
                mycursor.execute(com, val)  # Function to execute the command in mysql
                mydb.commit()  # This method is used to make sure the changes are consistent
                print("Account Updated")
                break
        else:  # If the Condition is not fulfilled ,for that purpose we ll use else statement
            print("Record not found")
    except:
        print("Table doesn't exist")


def delete():  # Function to delete details of a customer
    try:
        com = "select * from bank"
        mycursor.execute(com)  # Function to execute the command in mysql
        s = mycursor.fetchall()  # This function retrieves all rows of a query result
        j = input("Enter the Account Number whose details are to be deleted ")
        for i in s:  # For traversing through the list of record
            l = list(i)  # To convert into a list
            if l[0] == j:  # For traversing through each record
                m = l[0]
                cmd = "Delete from bank where accno={}".format(m)
                mycursor.execute(cmd)  # Function to execute the command in mysql
                mydb.commit()  # This method is used to make sure the changes are consistent
                print("Account deleted")
                break
        else:
            print(("Record not found"))
    except:
        print("Table doesn't exist")


def withdraw():  # Function to Withdraw the account by assuring the minimum balance of Rs.5000
    try:
        com = "select * from bank"
        mycursor.execute(com)
        s = mycursor.fetchall()
        print("Please note that the money can only be debited if minimum balance of Rs.5000 exists")
        acc = input("Enter account number from which the money is to be debited ")
        for i in s:
            l = list(i)
            if l[0] == acc:
                amt = int(input("Enter amount to be withdrawn "))
                if l[7] - amt >= 5000:  # To check if the balance amount is greater than Rs. 5000
                    l[7] -= amt
                    com = "UPDATE bank set balance={} where accno='{}'".format(l[7],l[0])
                    mycursor.execute(com)
                    mydb.commit()
                    print("Account debited")
                    break
                else:
                    print("there must be a minimum balance of Rs.5000")
                    break
        else:
            print("Record doesnt exist")
    except:
        print("Table doesn't exist")


def deposit():  # Function to credit money into the Account
    try:
        com = "select * from bank"
        mycursor.execute(com)
        s = mycursor.fetchall()
        acc = input("Enter the Account Number into which money is to credited  ")
        for i in s:
            l = list(i)
            if l[0] == acc:
                amt = int(input("Enter Amount to be credited  "))
                l[7] += amt
                com = "UPDATE bank set balance={} where accno='{}'".format(l[7],l[0])
                mycursor.execute(com)
                mydb.commit()
                print("Account credited")
                break
        else:
            print("Record not found")

    except:
        print("Table doesn't exist")


# MAIN CODE
while True:
    menu()
    ch = input("Enter your choice ")
    if ch == "1":
        Create()
    elif ch == "2":
        while True:
            menusort()
            ch1 = input("Enter choice a/b/c/d ")
            if ch1 in ["a", "A"]:
                dispsortacc()
            elif ch1 in ["b", "B"]:
                dispsortname()
            elif ch1 in ["c", "C"]:
                dispsortBal()
            elif ch1 in ["d", "D"]:
                print("Back to the Main Menu")
                break
            else:
                print("Invalid choice")
                break

    elif ch == "3":
        dispsearchacc()
    elif ch == "4":
        update()
    elif ch == "5":
        delete()
    elif ch == "6":
        while True:
            menutransaction()
            ch1 = input("Enter choice a/b/c ")
            if ch1 in ["A", "a"]:
                withdraw()
            elif ch1 in ["b", "B"]:
                deposit()
            elif ch1 in ["c", "C"]:
                print("Back to Main Menu")
                break
            else:
                print("Invalid Choice")
    elif ch == "7":
        print("Exiting......")
        break
    else:
        print("Wrong choice entered")