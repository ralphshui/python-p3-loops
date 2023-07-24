#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i>=1):
        print(i)
        i-=1
    print("Happy New Year!")

def square_integers(int_list): 
    int_list = [num * num for num in int_list]
    return int_list

def fizzbuzz():
    for num in range(1,101):
        if (num % 5 == 0) and (num % 3 == 0):
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)