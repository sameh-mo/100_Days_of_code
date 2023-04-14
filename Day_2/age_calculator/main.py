# calculate your age in years, months, weeks, Days
from datetime import date


# get year the user born in 
year = int(input("What year were you born?\n"))

# get the current year and subtract it form the year the user born in
age = date.today().year - year

# print the results
print(f"your age in years is {age}\n"
      f"your age in months is {age * 12} months\n"
      f"your age in Weeks is {age * 52} Weeks\n"
      f"your age in Days is {age * 365} Days")
