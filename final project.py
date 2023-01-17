#Challenge 1: Square Numbers and Return Their Sum
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
        return(a + b + c)
        pass


x = Point(1, 3, 5)
print(x.sqSum())


#Challenge 2: Implement a Calculator Class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num2 + self.num1)

    def subtract(self):
        return (self.num2 - self.num1)

    def multiply(self):
        return (self.num2 * self.num1)

    def divide(self):
        return (self.num2 / self.num1)


x = Calculator(10, 94)
print(x.add())
print(x.subtract())
print(x.multiply())
print(x.divide())

#Challenge 3: Implement the Complete Student Class

class Student:
    name = None
    rollNumber = None
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRollNumber(self, rollNumber):
        self.rollNumber = rollNumber

    def getRollNumber(self):
        return self.rollNumber


x = Student()
x.setName("dinesh")
print("Name:", x.getName())
x.setRollNumber(291120)
print("Roll Number:", x.getRollNumber())




#Challenge 4: Implement a Banking Account
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        
  
x = Account("name",500)
      
        
        
        
        
# Challenge 5: Handling a Bank Account


class Account:  
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    
    def withdrawal(self, amount):
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    



x = SavingsAccount("anish", 2000, 5)
x.withdrawal(500)
print("Balance after withdrawal:", x.getBalance())
x.deposit(1000)
print("Balance after deposit:", x.getBalance())
      





















