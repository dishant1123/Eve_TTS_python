"""bank app  : 

1. create  account :
    create  a  user name  : dishant 
    create  a  password  : dish@1211D    ===> 1 uppercase , 1 lowercase , 1 digit , 1 special character

2. login : 
        enter user name  : dishant 
        enter password  : dish@1211D
            ====> print  login success   ====> ac 25000 
            
1. deposit  
2. withdraw   : min balace 10000 maintain 
3. check balance 
4. exit 
"""

account = {}
def create_password(password):
    if len(password) >= 8:
        lower = False
        upper = False
        digit = False
        special = False

        special_char = "@#$%^&*"

        for ch in password:

            if ch.isupper():
                upper = True

            elif ch.islower():
                lower = True

            elif ch.isdigit():
                digit = True

            elif ch in special_char:
                special = True

        return upper and lower and digit and special
    return False

def create_account():

    print("\n------ Create Account ------")
    username = input("Enter Username : ")
    if username in account:
        print("Username already exists.")
        return
    password = input("Enter Password : ")
    if create_password(password):
        account[username] = {
            "password": password,
            "balance": 25000
        }
        print("Account Created Successfully.")
        print("Initial Balance : ₹25000")
    else:
        print("Invalid Password")


def login():

    print("\n------ Login ------")

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    if username in account:

        if account[username]["password"] == password:

            print("Login Successful")
            return username

        else:
            print("Incorrect Password")

    else:
        print("Username Not Found")

    return None


def deposit(username):

    amount = int(input("Enter Deposit Amount : "))

    if amount <= 0:
        print("Invalid Amount")
        return

    account[username]["balance"] += amount

    print("Deposit Successful")
    print("Current Balance :", account[username]["balance"])


def withdraw(username):

    amount = int(input("Enter Withdraw Amount : "))

    if amount <= 0:
        print("Invalid Amount")
        return

    if account[username]["balance"] - amount >= 10000:

        account[username]["balance"] -= amount

        print("Withdraw Successful")
        print("Remaining Balance :", account[username]["balance"])

    else:
        print("Minimum Balance of ₹10000 must be maintained.")


def check_balance(username):

    print("Current Balance :", account[username]["balance"])


def main():

    logged_user = None

    while True:

        print("\n========= BANK MENU =========")
        print("1. Create Account")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Exit")

        choice = int(input("Enter Choice : "))

        match choice:

            case 1:
                create_account()

            case 2:
                logged_user = login()

            case 3:
                if logged_user:
                    deposit(logged_user)
                else:
                    print("Please login first.")

            case 4:
                if logged_user:
                    withdraw(logged_user)
                else:
                    print("Please login first.")

            case 5:
                if logged_user:
                    check_balance(logged_user)
                else:
                    print("Please login first.")

            case 6:
                print("Thank You")
                break

            case _:
                print("Invalid Choice")


main()