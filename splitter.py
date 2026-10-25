
friends = int(input("How many friends are there? "))
bill = float(input("What is the total bill amount? "))

share = bill / friends
print("Each person's share is:", share)

for i in range(1, friends + 1):
    paid = float(input(f"How much did Friend {i} pay? "))

    difference = paid - share
    print("Difference:", difference)

    if difference == 0:
        print("Bill share settled")

    elif difference > 0:
        print("Friend should receive:", difference)

    else:
        print("Friend still owes:", abs(difference))

    print("--------------------")
