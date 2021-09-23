# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

#!Or
weight_as_int = int(weight)
height_as_float = float(height)

#TODO: Using the exponent operator
bmi = weight_as_int / height_as_float ** 2
#TODO: or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)