#!/usr/bin/env python3

import sys
#handling command-line arguments
for arg in sys.argv:
    continue
#determine name
name=arg
#definitions of different events 
def welcome():
    if len(name) > 0 and set(name).issubset(set(['0','1','2','3','4','5','6','7','8','9','+','%','/'])) is False and len(name) != 12:
        print("Hello " + name + "!")

def greet():
    if len(name) == 12:
        print("Hello World!")

def error():
    if set(name).issubset(set(['0','1','2','3','4','5','6','7','8','9','+','-','/','*','%','<','>'])) is True and len(name) != 0:
        print("Error!")
#definition of main() for simplifying
def main():
    welcome()
    greet()
    error()
#execution of main()
main()