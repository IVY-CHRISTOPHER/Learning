#Variable Manipulation

apple_price = 0.50
banana_price = 0.30
orange_price = 0.80

#suppose you want to buy 10 apples, 5 bananas and 8 oranges
total_cost = (10 * apple_price) + (5 * banana_price) + (8 * orange_price)
print("The total cost is: ", total_cost)

#suppose you are creating a user profile for a new online platform.
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

#!Process and format user inputs to create a summary report
#User Inputs
name = "Alice"
age = 30
hours_worked = 45.75
hourly_rate = 20.0

#Calculations
total_earnings = hours_worked * hourly_rate

#String Manipulation
report = f"Employee Name: {name}\nAge: {age}\nTotal Earnings: ${total_earnings:.2f}"
print(report)

#!Simple Budget Calculator
#User Inputs
income = 3000.00
rent = 800.00
utilities = 150.00
groceries = 200.00

#Calculations
total_expenses = rent + utilities + groceries
savings = income - total_expenses

#Output
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Savings: ${savings:.2f}")