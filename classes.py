class Person:
    def __init__(self,name,age,height,address,is_married):
        self.name = name #person1.name = "Alice"
        self.age = age #person1.age = 25
        self.height = height #person1.height = "170cm"
        self.address = address
        self.is_married = is_married #person1.is_married = False

    def greet(self):
        return f"Hi my name is {self.name}"


person1 = Person("Alice",25,"170cm","Kimathi St",False)
person2 = Person("Alvin",20,"178cm","Kimathi St",False)


print(person1)
print(type(person1))
print(person1.name) 
print(person1.address)

print(person1.greet())
print(person2.greet())


class BankAccount:
    def __init__(self, Account_number, owners_name, date_opened,balance=0):
        self.account_number = Account_number
        self.balance = balance
        self.owners_name = owners_name
        self.date_opened = date_opened
        print("Welcome")

    def deposit(self, amount):
        amount = float(input("Enter the Amount you want to deposit: "))
        if amount < 0:
            print("you can't deposit a negative amount")
        else:
            self.balance += amount
        print(f"You have deposited Ksh. {amount}")
        

    def withdraw(self, amount):
        amount = float(input("Enter the Amount you want to withdraw: "))
        if self.balance < amount:
            print("insufficient funds")
        else:
            self.balance -= amount
            print(f"You have withdrawn Kshs. {amount}")


    def display_info(self):
        print(f"Your Acc no is Kshs. {self.account_number}")
        print(f"Your Available Balance is Kshs. {self.balance}")
        print(f"Owner's name is {self.owners_name}")
        
                    
account1 = BankAccount("EQ12345","Henry Mwangi",500)
account1.deposit(10000)
account1.withdraw(3000)
account1.display_info()
                    


        
            