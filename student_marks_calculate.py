print("Welcome let's calculate your marks!!!!")
Name = input("Enter your name: ")
Reg_no = int(input("Enter your reg no: "))
sub_1 = int(input("Enter the mark of the first subject: "))
sub_2 = int(input("Enter the mark of the second subject: "))
sub_3 = int(input("Enter the mark of the third subject: "))

if (sub_1 < 0 or sub_1 > 100 or 
    sub_2 < 0 or sub_2 > 100 or 
    sub_3 < 0 or sub_3 > 100):
    print("Invalid marks cannot be negative or greater than 100")
else:
    total = sub_1 + sub_2 + sub_3
    print(f"The total is {total}")
    
    average = total / 3
    print(f"The average is {average}")
    
    if average >= 90:
        print("Grade A")
    elif average >= 75:
        print("Grade B")
    elif average >= 50:
        print("Grade C")
    else:
        print("Grade D / Fail")    