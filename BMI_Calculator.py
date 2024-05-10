height = float(input("Enter your height in centimeters(cm): "))
weight = float(input("Enter your weight in kilogram(kg): "))

height = height/100

BMI = round(weight/(height*height),2)

print("Your Body Mass Index(BMI) is: ",BMI)

if(BMI>0):
    if(BMI<=16):
        print("You are severely underweight!")
        
    elif(BMI<=18.5):
        print("You are underweight!!")
        
    elif (BMI<=25):
        print("Congratulations!!! You are healthy.")
        
    elif (BMI<=30):
        print("Alas! You are overweight!")
    
    else:
        print("Sorry, your are severely overweight!")
        
else:
    print("Please provide valid details.")