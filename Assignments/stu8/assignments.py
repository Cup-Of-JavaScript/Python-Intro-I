#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python I
#


def ex1():
    hello_world("4")


def ex2():
    array = [1, 2, 3]
    array_to_string(array)


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

def hello_world(y):
    x = int(y)
    for x in range(x):
        print("Hello World from Python!")

def array_to_string(array):
    result = ' '.join(str(x) for x in array)
    print(result)

def add_numbers(array):
    result=0
    for x in array:
        result += float(x)
    print(result)