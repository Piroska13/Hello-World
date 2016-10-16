#!/usr/bin/env python3

import sys
#handling command-line arguments
for arg in sys.argv:
    continue
#determine name
name=arg
#definitions of different cases 
def welcome():
    '''If the wrote name is more, than 0, 
    isn't a matematical symbol and 
    isn't the length of it 12, 'Hello name!' will be printed!'''
    if len(name) > 0 and set(name).issubset(set(['0','1','2','3','4','5','6','7','8','9','+','-','/','*','%','<','>'])) is False and len(name) != 12:
        print("Hello " + name + "!")

def greet():
    ''' If the wrote name's length is 12,
    'Hello World!'' will be printed. ''' 
    if len(name) == 12:
        print("Hello World!")

def error():
    ''' If the wrote name is one or more mathematical symbols,
    'Error!' will be printed. ''' 
    if set(name).issubset(set(['0','1','2','3','4','5','6','7','8','9','+','-','/','*','%','<','>'])) is True:
        print("Error!")

def main():
    #definition of main() for simplifying, which include all cases
    welcome()
    greet()
    error()
#execution of main()
main()