#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python I
#
from typing import Any


def ex1():
    hello_world("3")


def ex2():
    array = [1, 2, 3]
    result = array_to_string(array)
    print(result)





def ex3():
    array = [1.0, 1.1, "1"]
    add_numbers(array)




def ex4():
    print("TODO: Ex. 4...")


def ex5():
    print("TODO: Ex. 5...")


def ex6():
    print("TODO: Ex. 6...")


def ex7():
    print("TODO: Ex. 7...")


def ex8():
    print("TODO: Ex. 8...")


def ex9():
    print("TODO: Ex. 9...")


def ex10():
    print("TODO: Ex. 10...")


def ex11():
    print("TODO: Ex. 11...")


def ex12():
    print("TODO: Ex. 12...")


def ex13():
    print("TODO: Ex. 13...")


def ex14():
    print("TODO: Ex. 14...")


def ex15():
    print("TODO: Ex. 15...")


#
# Place your functions here...
#

def hello_world(x):
    i =int(x)
    for i in range(i):
        print("Hello World from Python!")

def array_to_string(array):
    string = ''
    for numbers in array:
        string += ''.join(str(numbers) for numbers in array)
        return string

def add_numbers(array):
    sum =0
    for numbers in array:
        sum += float(numbers)
    print(sum)













