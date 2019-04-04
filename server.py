weight = int(input("what is you weight in kg? "))
age = int(input("what is your age? "))
height = int(input("what is your height in inches? "))
time = int(input("what was your running time? "))
if weight < 60 and age > 17 and height > 50 and time < 50:
    
    print("Welcome to the Fatimiyah College sports team")
else:
    print("Sorry you are not eligible for team")
