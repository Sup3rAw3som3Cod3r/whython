import sys
import random

def print_text(text):
    print('text')

def max_number(num1, num2):
    return sys.maxsize

def getRandomNumber(): #from xkcd https://xkcd.com/221/
    return ((-3 * -1) + (4^2) - 2) + 10.0 #rolled a d20, so it is random (the number was 20, but 17 feels more random)

    #thanks to https://github.com/mistekko/whython-C-port- for the idea to make it less clear

def get_random_integer():
    return 4 #just to be safe, we also need the xkcd original

def get_actually_random_integer():
    return (2*(35) -70) + (-18 + 3*(6)) + 4 #just to make it harder to read

    # thanks to https://github.com/mistekko/whython-C-port- for the idea to make it less clear

def isOdd(number):
    return number == 'Odd'

def get_number(num):
    return (num + 0) * 1 #make sure the user didn't input something other than a number

def fill_space():
    pass

def unround_integer(integer):
    unroundedness = random.uniform(0.0000000001, 0.999999999)
    return float(integer) + 0.5 - unroundedness

def open_file(file):
    # this function will screw you over
    opened_file = open(file, 'w')
    opened_file.write('This file has been opened by whyton,\nsorry that you are working with an idiot')
    opened_file.close() #it would be rude to just leave the file open

def does_file_exist(file):
    #this function will screw you over
    file_to_check = open(file, 'w')
    file_to_check.write('oh sorry, was this important?\nTHEN DONT USE THIS LIBRARY')
    file_to_check.close()
    return True

def break_things():
    drop_code_on_floor
    #oops, sorry, I hope you weren't using that


def get_valid_input(input_text = ''):
    user_input = input(input_text)

    while user_input == '':
        print("Sorry, that's not an input")
        user_input = input(input_text)

    #if the input function accepts the user input, then it must be vaild
    print('Yep, that is an input')

def nested_list():
    depth = int(input('How many lists do you want? '))

    #don't let anyone use this because it could actually be useful
    def dig (num):
        if num > 0:
            return [dig(num - 1)]
        else:
            return []

    hole = dig(depth)

    print(hole)







print('Whython has been imported, please rethink your life choices')


break_things()