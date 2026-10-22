print("Hello and welcome to Sowmi's quiz session now i will ask you three qns and if you answer any three correctly then i will give you a choclate!!!!!!!!")
name = input("Enter your name:  ")
print("Hello,",name)
score = 0

answer_1 = input("What is called as the rainbow colour")
if answer_1.lower() == "vibgyor":
    print("Woah you are right")
    score = score + 1
    print(score)
else:
    print("Thats ok you still have 2 qns ")
    
answer_2 = input("When is human right's day celebrated (just give the month): ")   
if answer_2.lower() == "december":
    print("Woah you got it right again")
    score = score + 1
    print(score)
else:
    print("Thats ok you have 1 more qn")
    
answer_3 = input("Which planet in our solar system is famously known as the 'Red Planet'?: ")   
if answer_3.lower() == "mars":
    print("Woah you got it right again")
    score = score + 1
    print(score)
else:
    print("Better luck next time") 
    
print(f"Your total score is {score}")

if score == 3:
    print("Here you go your🍫")
else:
    print("Better luck next time")