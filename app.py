# BMI = lb / (in)^2 * 703
#bmi = print(170 / 62 ** 2 * 703)
# 18.5 - 24.9 = healthy, 25.0 - 29.9 = overweight, > 30 obesity

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
import pandas

# with open("my_file.txt", mode="a") as file:
#     file.write(f"\n{bmi}")

height = float(input("Enter your height in inches?: "))
weight = float(input("What is your weight in lbs?: ")) 
bmi = (round(weight / height ** 2 * 703, 2)) 

if bmi <= 18.5:
    print(f"Your BMI is {bmi}. You are UNDERWEIGHT. Eat some cornbread")
elif bmi <= 24.9:
    print(f"Your BMI is {bmi}. You are a HEALTHY weight. Keep up the good work! Stay between 18.5 - 24.9.")
elif bmi <= 29.9:
    print(f"Your BMI is {bmi}. You are OVERWEIGHT. Your BMI should be between 18.5 - 24.9.")
    print("A BMI of 28+ is linked to a higher risk of Type II Diabetes for Black people")
    print("Increase calories spent and decrease calories eaten")
elif bmi <= 39.9:
    print(f"Your BMI is {bmi}. You are OBESE.")
else:
    print(f"Your BMI is {bmi}. You are MORBIDLY OBESE")
    print("Put down the ice cream and see your Healthcare Provider IMMEDIATELY.")

