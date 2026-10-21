birth_year = int(input("Whats your birth year: "))
current_year = int(input("Enter the current year: "))
if birth_year > 2026:
    print("Oops invalid year cannot calculate age")
else:
    age = current_year - birth_year
    print(f"Your age is {age} ")
    

if age <18 :
    print("You are still a minor")
else:
    print("You are a major now happy 18")
    
age_100 = 100 - age
print(age_100)

year_to_100 = current_year + age_100
print(year_to_100)

print(f"You will turn hundred years at {year_to_100}")