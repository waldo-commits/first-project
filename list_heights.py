height = input("Enter 4 heights with seperate spaces: ")
my_list = height.split(",")
print(my_list)
total_sum = 0
for i in my_list:
    total_sum = total_sum + int(i)
    print(total_sum)
print(f"The final total is {total_sum}")
average = total_sum/4
average = round(average)
print(f"The average is {average}")
    
    