# solution_1
print("\n____________solution_1___________\n")
class Rectangle():
    def __init__(this, width, height):
        this.witdh = width
        this.height = height

    def area(this):
        area = this.witdh*this.height
        return area
    def perimeter(this):
        perimeter = 2*(this.witdh+this.height)
        return perimeter
    
rectangle = Rectangle(5,7)
print(f"the area of the rectangle: {rectangle.area()}\nthe perimeter of the rectangle: {rectangle.perimeter()}")

# solution_2
print("\n____________solution_2___________\n")

# solution_3
print("\n____________solution_3___________\n")

# solution_4
print("\n____________solution_4___________\n")

# solution_5
print("\n____________solution_5___________\n")

class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"\ncustomer name and surname: {self.name} {self.surname}\ncustomer T.C number: {self.tc}\ncustomer phone number: {self.phone}")

class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone, account_number, balance):
        super().__init__(name, surname, tc_identification, phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit successful!")
    def money_check(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print("Transaction successful!")
        else:
            print(f"\nYour account does not have sufficient balance. Please enter a different amount or deposit money into your account!")
    def display_balance(self):
        print(f"Your total account balance: {self.balance}")

Info = Account("Eren","Karaca", '123456', '05123456','789456456',100)

def menu(Info):
    while True:
        print("\n1- Deposit money 2- Withdraw money 3-View account balance 4-View account information  0-Exit")
        while True:
            try:
                choice = int(input("\nPlease select the operation you want to perform: "))
                if -1< choice <5:
                    break
                else:
                    print("invalid number please try again!")
            except ValueError:
                print("please enter a number!")

        if choice == 0:
            break
        elif choice == 1:
            amount = float(input("please enter amount to deposit: "))
            Info.deposit(amount)
        elif choice == 2:
            amount = float(input("please enter amount to withdraw: "))
            Info.money_check(amount)
        elif choice == 3:
            Info.display_balance()
        elif choice == 4:
            Info.display_information()

menu(Info)
        



  





