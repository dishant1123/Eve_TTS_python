"""
bank app  : 

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

account ={}

def create_password(password):
    
    if len(password)>=8 :
        lower =False
        upper =False
        digit =False
        special =False
        
        special_char =["@","#","$","%","^","&","*"]
        
        for  i in password :
            if  i.isupper() :
                upper =True
            elif  i.islower() :
                lower =True
            elif  i.isdigit() :
                digit =True
            elif  i in special_char :
                special =True
        
        if  upper and lower and digit and special :
            return True
        else :
            return False
    else :
        return False

def create_account():
    
    print("----------create account ----------")
    
    username =input("enter username : ")
    password =input("enter password : ")
    
    if  create_password(password) :
        account[username]=password
        print("account created successfully")
    else :
        print("password is not valid")
        
def login():
    username =input("enter username : ")
    password =input("enter password : ")
    
    if username in account :
        if account[username]==password :
            print("login success")
            # account[username]=25000 
        else: 
            print("password is not valid")
    else :
        print("username is not valid") 
        
def deposit(username):
    amount =int(input("enter amount : "))
    
    if amount<0 :
        print("amount should be positive")
    else :
        if username in account :
            account[username]['balance']+=amount
            print("deposit success")
    
        
def withdraw(username):
    amount =int(input("enter amount : "))  # 20000
    if amount<0 :
        print("amount should be positive")
    else :
        if username in account :
            if account[username]['balance']>=amount :# 5000 > 20000 
                account[username]['balance']-=amount
                print("withdraw success")
        else :
            print("username is not valid")
        
    
def check_balance(username):
    print("your  final balance is  : ",account[username]['balance'])    
def main():
    while True :
        print("1. create account")
        print("2. login")
        print("3. deposit")
        print("4. withdraw")
        print("5. check balance")
        print("6. exit")
        choice =int(input("enter choice : "))
        match choice :
            case 1 :
                create_account()
            case 2 :
                login()
            case 3 :
                deposit()
            case 4 :
                withdraw()
            case 5 :
                check_balance()
            case 6 :
                break
                
main()

