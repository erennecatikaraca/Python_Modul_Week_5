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
class School:

    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}
#Aynı isimli öğrenciler olabileceği için liste daha esnek bir yapı sunar. bu yuzden liste yapisi kullaniyorum.

#Hızlı Erişim (Key-Value): Öğretmenlerin branşıyla birlikte kaydedilmesi gerektiği için,
# bir öğretmen adına hızlıca erişmek adına sözlük daha uygundur.
# Sözlüklerde anahtar (key) olarak öğretmen adı, değer (value) olarak da branşıni kaydediyorum.

    def add_new_student(self, student_name, student_class):
        self.students.append((student_name, student_class))
        print(f"The student named {student_name} has been added to the {student_class} class.")

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch
        print(f"The teacher named {teacher_name} was added with the branch {branch}.")

    def view_student_list(self):
        print("\n___Student List___")
        for student_name, student_class in self.students:
            print(f"- {student_name} ({student_class})")

    def view_teacher_list(self):
        print("\n___Teacher List___")
        for teacher_name, branch in self.teachers.items():
            print(f"- {teacher_name} ({branch})")

    def __str__(self):
        return f"School Name: {self.name}, Founded in: {self.foundation_year}, Students: {len(self.students)}, Teachers: {len(self.teachers)}"


# Kullanıcıdan okul bilgilerini almak icin input kullaniyorum.
school_name = input("Enter the school name: ")
foundation_year = int(input("Enter the foundation year: "))
my_school = School(school_name, foundation_year)

# Öğrenci eklemek icin while dongusu kullaniyorum.
while True:
    add_student = input("Do you want to add a student? (yes/no): ").lower()
    if add_student == "yes":
        student_name = input("Enter the student's name: ")
        student_class = input("Enter the student's class: ")
        my_school.add_new_student(student_name, student_class)
    elif add_student == "no":
        break
    else:
        print("Please type 'yes' or 'no'.")


while True:
    add_teacher = input("Do you want to add a teacher? (yes/no): ").lower()
    if add_teacher == "yes":
        teacher_name = input("Enter the teacher's name: ")
        branch = input("Enter the teacher's branch: ")
        my_school.add_new_teacher(teacher_name, branch)
    elif add_teacher == "no":
        break
    else:
        print("Please type 'yes' or 'no'.")

# Okul ve listeleri ekrana yazdırmak icin print kullaniyorum.

print(f"\n{my_school}")

my_school.view_student_list()

my_school.view_teacher_list()

# solution_3
print("\n____________solution_3___________\n")
class Shape():

    def __init__(self, width, height):
        self.width=width
        self.height=height  

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height
    
class Square(Shape):
    def calculate_area(self):
        return self.width ** 2
    
rectangle = Rectangle(30, 2)
square = Square(3, 3)

print(rectangle.calculate_area())
print(square.calculate_area())

# solution_4
print("\n____________solution_4___________\n")

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Off_Road_Vehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.fourwheeldrive = four_wheel_drive
        if self.fourwheeldrive=="Yes":
            self.fourwheeldrive="The vehicle has four-wheel drive."
        else:
            self.fourwheeldrive="The vehicle has not four-wheel drive."


vehicle1=Off_Road_Vehicle("Toyota","Hilux","2010","No")
print(f"Off Road Vehicle\nMake:{vehicle1.make}\nModel:{vehicle1.model}"
      f"\nYear:{vehicle1.year}\nFour Wheel Drive:{vehicle1.fourwheeldrive}")
class SportCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

sportCar1=SportCar("Porche","911 Turbo S","2024",330)

print(f"\nSport Car\nMake:{sportCar1.make}\nModel:{sportCar1.model}"
      f"\nYear:{sportCar1.year}\nMaximum Speed:{sportCar1.max_speed}")

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
        if self.balance >= amount:
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
        



  





