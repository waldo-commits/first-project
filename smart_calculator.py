a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operators = input("Enter an operator like '+','-','/','*'")
if operators == '+':
    print(a+b)
elif operators == '-':
    print(a-b)
elif operators == '*':
    print(a*b)
elif operators == '/':
   if b != 0:
       print(a/b)
   else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
