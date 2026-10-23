print("Hello welcome to Sowmi's Bank!!")
correct_code = 1012
attempts = 0 
while attempts < 3:
    password = int(input("Enter the pin number of your card: "))
    if password == correct_code:
        print("The code is correct ")
        break
    else:
        print("Wrong code")
        attempts = attempts +1
if attempts == 3:
    print("You are out of attempts")
