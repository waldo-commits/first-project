import random

numbers = random.randint(1, 10)
attempts = 0
max_attempts = 3

while attempts < max_attempts:
  user_input = int(input("Enter a random number between 1 to 10: "))
  attempts = attempts + 1

  
  if numbers == user_input:
    print("Woah you got it right!!!!!!")
    break  
  elif numbers < user_input:
    print("Go lower")
  else:
    print("Go higher")
    
Remaining = max_attempts - attempts
print(f"The remaining attempts is{Remaining}")

if attempts == max_attempts and user_input != numbers:
  print("Game over")    
    