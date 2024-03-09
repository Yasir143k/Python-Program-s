height = float(input("Enter Your Hight! ")) #in inches e.g 1.5
weight = int(input("Enter Your Weight! ")) #in kilogram e.g 72
#formula to calculate BMI
BMI = weight / (height * height) 
if BMI < 18.5:
    print(f"Your BMI is {BMI},you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI},you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI},you are slightly overWeight.")
elif BMI < 35:
    print(f"Your BMI is {BMI},you are obese.") #obese means vary fat
else:
    print(f"Your BMI is {BMI},you are clinicaly obse.")