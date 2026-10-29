class ATM:
    def __init__(self):
        self.__balance=0
        self.pin=''
        self.menu()
    def __str__(self):
        return "Welcome to SBI ATM"
    def menu(self):
        while True:
            user=input(""" What can we help you with?
        1. Create pin
        2. Withdraw
        3. Deposit
        4. Check balance
        5. exit
""")
            if user=="1":
                self.create_pin()
            elif user=="2":
                self.withdraw()
            elif user=="3":
                self.deposit()
            elif user=="4":
                self.check_balance()
            else:
                print("byee")
                break
    def create_pin(self):
       self.pin=input("Enter pin you want to set: ")
       print("pin created successfully")

    def withdraw(self):
        amount=int(input("Enter the amount you want to withdraw:  "))
        if amount<self.__balance:
            self.__balance=self.__balance-amount
            print(amount,"withdrawn successfully")
        else:
            print("oh! ohh! not enough balance")

    def deposit(self):
        amount=int(input("Enter the amount you want to deposit:  "))
        self.__balance=self.__balance+amount
        print(amount,"deposited successfully")

    def check_balance(self):
        print("balance is",self.__balance)


sbi=ATM()
sbi._ATM__balance="897897"