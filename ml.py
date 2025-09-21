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



# # Word Frequency Counter Program

# def word_frequency(text):
#     # Text ko lowercase kar ke aur split karke words nikalna
#     words = text.lower().split()
    
#     # Dictionary for storing frequencies
#     freq = {}
    
#     for word in words:
#         # Agar word dictionary me hai to +1 karo warna 1 se start karo
#         freq[word] = freq.get(word, 0) + 1
    
#     return freq


# # User input
# text = input("Enter some text: ")

# # Function call
# result = word_frequency(text)

# # Display result creatively
# print("\n Word Frequency Count")
# for word, count in result.items():
#     print(f"{word} : {count}")



import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game 🐍")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()
            score = 0
            delay = 0.1

            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
