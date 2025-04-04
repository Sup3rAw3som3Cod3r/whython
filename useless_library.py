import sys
import random

def print_text(text = ''):
    print('text')

def max_number(num1, num2):
    return sys.maxsize

def getRandomNumber(): #from xkcd https://xkcd.com/221/
    return 17.0 #rolled a d20, so it is random (the number was 20, but 17 feels more random)

def get_random_integer():
    return 4 #just to be safe, we also need the xkcd original

def isOdd(number):
    return number == 'Odd'

def get_number(num):
    return num + 0 #make sure the user didn't input something other than a number

def fill_space():
    pass

def unround_integer(integer):
    unroundedness = random.uniform(0.0000000001, 0.999999999)
    return float(integer) + 0.5 - unroundedness

print(f'Why are you doing this to yourself?')
print(f'Please never use this library.')
print()

