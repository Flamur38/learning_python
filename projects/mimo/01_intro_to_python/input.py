# this code will ask the user for their name
print("What's your name?")

name_input = input()
print(f"Hi, {name_input}")

# Output:
# What's your name?                                                                                      
# flamy                                                                                                  
# Hi, flamy

print('----')

user_input = input("Enter your name: ")
print(f'Thanks, {user_input}')
# Output
# Enter your name: flamy                                                                                 
# Thanks, flamy

print('---')

# conver string to int
user_input_1 = input("Enter a number: ")
user_input_2 = input("Enter another number: ")
number1 = int(user_input_1)
number2 = int(user_input_2)
result = number1 + number2 
print(f"The sum is {result}")
print(type(user_input_1))
print(type(number1))

print("---------" )

# check if user is 21 or older
age = input("Enter your age: ")
if (int(age) < 21):
    print("Under 21")
else:
    print("21 or older")

print("----")

# multiple inputs
name = input("Hello what is your name? ")
print(f"Nice to meet you, {name}!")
age_input = input("How old are you? ")
age = int(age_input)
bot_age = 3
age_difference = age - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")
color = input("What's your favorite color? ")
print(f"Oh, {color} is a beautiful color!")
