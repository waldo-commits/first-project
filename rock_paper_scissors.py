import random

# Get user input and immediately convert it to uppercase (e.g. "scissors" becomes "SCISSORS")
a = input("Hi choose among rock paper and scissors: ").upper()

b = "ROCK PAPER SCISSORS"
b_new = b.split()
print("Computer choices list:", b_new)

c = random.choice(b_new)
print("Computer chose:", c)

# Now compare uppercase text with uppercase choices
if a == c:
    print("Woah it is a tie!")
elif a == "ROCK" and c == "SCISSORS":
    print("You won!")
elif a == "PAPER" and c == "ROCK":
    print("You won!")
elif a == "SCISSORS" and c == "PAPER":
    print("You won!")
else:
    print("The computer wins!")
