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
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}, new balance = {self.balance}")
    
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn {amount}, balance left = {self.balance}")
#         else:
#             print("Insufficient Balance!")

# # Using the class
# acc1 = BankAccount("Zunaira", 500)
# acc1.deposit(200)
# acc1.withdraw(100)


# import time

# # Palindrome Checker (Creative Coding)

# # User input
# text = input("Enter a word or number: ")

# # Remove spaces + lowercase for fair comparison
# clean_text = text.replace(" ", "").lower()

# # Reverse the string
# reversed_text = clean_text[::-1]

# print("\n Checking if it's a palindrome...\n")
# time.sleep(1)

# # Print characters one by one (animation effect)
# for c in reversed_text:
#     print(c, end="", flush=True)
#     time.sleep(0.1)
# print("\n")

# # Palindrome check
# if clean_text == reversed_text:
#     print(f"Wow! '{text}' is a Palindrome")
# else:
#     print(f"'{text}' is NOT a Palindrome.")



# Word Frequency Counter Program

def word_frequency(text):
    # Text ko lowercase kar ke aur split karke words nikalna
    words = text.lower().split()
    
    # Dictionary for storing frequencies
    freq = {}
    
    for word in words:
        # Agar word dictionary me hai to +1 karo warna 1 se start karo
        freq[word] = freq.get(word, 0) + 1
    
    return freq


# User input
text = input("Enter some text: ")

# Function call
result = word_frequency(text)

# Display result creatively
print("\n Word Frequency Count")
for word, count in result.items():
    print(f"{word} : {count}")
