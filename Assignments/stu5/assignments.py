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
    sentence = input("Enter sentence: ")
    num_words = count_words(sentence)
    print(num_words)



def ex5():
    sentence = "Test.  This is a test.  Testing."
    sentence2 = replace_period(sentence)
    print(sentence2)




def ex6():
    array = ["this", "is", "another", "test"]
    slice_it(array)






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
        string += str(numbers)
    return string



def add_numbers(array):
    sum =0
    for numbers in array:
        sum += float(numbers)
    print(sum)

def count_words(sentence):
     retval= len(sentence.split())
     return retval

def replace_period(sentence):
    retval = sentence.replace (".", "!")
    return retval

def slice_it(array):
    retval=""
    for i in array:
        retval += str(i[:2])
    print(retval)



     # retval = str(array[:2])
     # return retval





















