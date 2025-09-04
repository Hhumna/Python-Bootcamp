weight = float(input("weight: "))
height = float(input("height: "))
bmi = weight / (height ** 2)
print(weight, " / ", height, " * ", height, bmi)
bmi = round(bmi)

if(bmi < 18.5):
    print("Your BMI is ", bmi, ", you are underweight.")
elif(18.5 <= bmi < 25):
    print("Your BMI is ", bmi, ", you have a normal weight.")
elif(25 <= bmi < 30):
    print("Your BMI is ", bmi, ", you are overweight.")
elif(30 <= bmi < 35):
    print("Your BMI is ", bmi, ", you are obese.")
elif(bmi >= 35): 
    print("Your BMI is ", bmi, ", you are clinically obese.")  
