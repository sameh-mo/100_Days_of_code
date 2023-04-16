# leap year detector program

#welcome screen
print("welcome to leap year detector program")

# prompt to get the year
year = int(input("Enter the year please: "))

# leap year checker function
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# message

if leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year ")
