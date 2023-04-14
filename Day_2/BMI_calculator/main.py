# BMI calcualtor

# getting user height and weight in (m, kg)
height = float(input("Enter the height in Meter: "))
weight = float(input("Enter the weight in KG: "))

# calculating BMI weight/ hight^2
bmi = round(weight / (height **2), 2)

# output the result
print(f"your BMI is {bmi} \ngreat job your BMI is ideal!" if 18.5 < bmi < 24.9 else f"you need to enhance your BMI {bmi} ^_^")