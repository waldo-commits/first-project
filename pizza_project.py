print("Hello welcome to Sowmi's pizza shop ")
print("What would you like to order? (small/medium/large)")
Bill = 0
pizza = input().strip().lower()
if pizza == "small":
    Bill = 100
    print("The cost is 100 rs")
elif pizza == "medium":
    Bill = 200
    print("The cost is 200 rs ")
else:
    Bill = 300
    print("The cost is 300 rs")
    
mushrooms =input("Do you want mushrooms (Y/N):")    
if mushrooms == 'y' or mushrooms  == 'Y':
    if pizza == "small":
         Bill = Bill+30
    else:
        Bill = Bill+50
paneer =input("Do you want paneer (Y/N):")    
if paneer == 'y' or paneer == 'Y':
    if pizza == "small":
         Bill = Bill+30
    else:
        Bill = Bill+50 
        
want_cheese= input("Do you want cheese? (y/n)")
if want_cheese == 'Y' or want_cheese == 'y':
    Bill = Bill+20
    print(f"Your total bill is {Bill}")
    
bread_sticks=input("Do you want a side of  breadsticks (y/n) ")
if bread_sticks == 'y' or bread_sticks == 'Y':
    Bill= Bill+60
    print(f"Your total bill is {Bill}")
fries=input("Do you want a side of fries (y/n) ")
if fries == 'y' or fries == 'Y':
    Bill= Bill+45
    print(f"Your total bill is {Bill}")    
    
brownie= input("Do you want a two piece brownie")
if brownie == 'y' or brownie == 'Y':
   Bill = Bill+75
   print(f"Your total bill is {Bill}")
         
        

    
    