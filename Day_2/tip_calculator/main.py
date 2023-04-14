# Tip calculator
# welcome screen
print ("welcome to the Tip calculator")
# get the total bill
total_bill = float(input("Enter the total bill: $"))

# get number of people to split the bill
n_persons = int(input("Enter number of persons: "))

# get tip percentage they want to pay
tip_perc_of_total_bill = float(input("Enter the percentage of tip you would like to pay: %")) / 100

# the tip each person should pay
tip_per_person = round(((total_bill * tip_perc_of_total_bill) / n_persons),2)

# print how much each person should pay as a tip
print(f"the tip each person should pay is ${tip_per_person}")
