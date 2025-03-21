import math

print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
tipPercentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

possibleTips = [10, 12, 15]
while tipPercentage not in possibleTips:
    tipPercentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

tipAmount = totalBill / 100 * tipPercentage
peopleAmount = int(input("How many people to split the bill? "))

result = round((totalBill + tipAmount) / peopleAmount, 2)
print(f"Each person should pay: ${round((totalBill + tipAmount) / peopleAmount, 2)}")