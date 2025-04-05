#Converting Strings to Nums
num_string = "123"
num_integer = int(num_string)
print(num_integer) #Outputs 123

#Converting Nums to Strings
age = 30
message = "I am " + str(age) + " years old."
print(message) #output: I am 30 years old.

#User Inputs are always saved as a string
#So you must convert them to a number to do arithmetic operations
user_input = input("Enter a number: ")
number = int(user_input)
doubled_number = number * 2
print("Your number doubled is:", doubled_number)

salary_str = "50000"
bonus = 5000

#Attempting to add without conversion would result in a typeError
#total_income = salary_str + bonus 
#Raises TypeError

#Correct way with explicit conversion
total_income = int(salary_str) + bonus
print("Total Income:", total_income) #Output: Total income: 55000

#Python will handle typecasting on its own in some cases where there is no risk of losing information
integer_number = 10
float_number = 5.5
result = integer_number + float_number
print(result) #Output: 15.5
print(type(result)) #Output: <class 'float'>

#Real world example
#Changing a data tuple into a dictionary for better readability
data_tuples = (('name', 'Alice'), ('age', 25), ('city', 'Wonderland'))
data_dict = dict(data_tuples)
print(data_dict)
#Outputs: {'name': 'Alice', 'age': 25, 'city': 'Wonderland}

#Complex data types
ascii_value = 65
char = chr(ascii_value)
print(char)
#output: A