print("My Python Assignment 1 from Blockchain Course by Academind")
# Follow the instructions explained in the problem video and try to implement a solution on your own.

# My Solution
# 1) Create two variables one with your name and one with your age
myName = "Mic"
myAge = 32


"""
# 2) Create a function which prints your data as one string

def user_data():
    print('Name is ', myName, 'and age is' ,  myAge, 'years old.')
user_data()

print("******************************")
print("Create your cryprocurrency")
print("\n")
# 3) Create a function which prints ANY data (two arguments) as one string
coin_name = input('Enter coin name: ')
coin_maker  = input('Enter name of creator: ')
def any_coins(param1, param2):
    print('Coin: ' + param1 + ' \n Created by ' + param2)
    print("\n Congrats! You just created a new crypto")
any_coins(coin_name, coin_maker)

"""
print("******************************")
# 4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
user_age = input('Enter your age: ')

def calculate_life(user_age):
    number_of_decades_lived = user_age // 10
    return number_of_decades_lived


decades = calculate_life(int(user_age))
print(decades)

