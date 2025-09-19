# print("Start Machine Learning")

# #Sum Program 

# print("Welcome to the Magical Addition Machine")
# print("Two numbers will go in... and their magical sum will come out!")

# # Asking user for input
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# # Performing sum
# sum_result = num1 + num2

# # Fun, creative output
# print("\n Mixing the powers of", num1, "and", num2, "...")
# print("Drumroll please")
# print("The magical sum is:", sum_result,)


# # Squares from 1 to 10 

# print("Welcome to the Square Show! \n")

# for i in range(1, 11):
#     print(f"{i} × {i} = {i*i}")






# # Word Reverser 

# print("Welcome to the Magical Word Reverser \n")

# word = input("Enter any word: ")

# reversed_word = word[::-1]

# print("\n Casting a spell. reversing the letters")
# print("Original Word:", word)
# print("Reversed Word:", reversed_word)
# print("Ta-da! Your word has been flipped!")



#Create a bank account app 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance = {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}, balance left = {self.balance}")
        else:
            print("Insufficient Balance!")

# Using the class
acc1 = BankAccount("Zunaira", 500)
acc1.deposit(200)
acc1.withdraw(100)




