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
    r = slice_it(array)
    print(r)







def ex7():
    array = [2.00, 4.00, 4.00]
    tax = "10%"
    calc_total(array, tax)



def ex8():
    c = -6
    f = 22
    f_to_c(22)
    c_to_f(-6)

def ex9():
    sentence = "This is a test"
    num_vowels = vowel_counter(sentence)
    print(f"Number of vowels: {num_vowels}")


def ex10():
    while True:
        result = calculator()
        print(result)
        break




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
        retval += (str(i[:2]))
    return retval

def calc_total(array, tax):
    result = 0
    for x in array:
        result += float(x)
        number = result * int(tax[:1])*0.10
        dollar_number = "${:,.2f}".format(number + result)
    print(dollar_number)


def c_to_f(c):

     f = int((c * 9/5) + 32)
     print( f"{c} degrees Celsius is {f} degrees Fahrenheit.")

def f_to_c(f):
    c = int((f - 32) * 5/9)
    print( f"{f} degrees Fahrenheit is {c} degrees Celsius.")

def vowel_counter(sentence):
    vowel=0
    for char in sentence:
        if char in "aeiouAEIOU":
            vowel = vowel+1
    return vowel

def calculator():
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y
    def multiply(x,y):
        return x*y
    def divide(x,y):
        return(x/y)

    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    operator = input("Enter operation (+, *, /, -): ")

    if operator == '+':
        # print(num1, "+", num2, "=", add(num1, num2))
        return( add(num1, num2))

    elif operator == '-':
         #print(num1, "-", num2, "=", subtract(num1, num2))
         return(subtract(num1, num2))

    elif operator == '*':
        #print(num1, "*", num2, "=", multiply(num1, num2))
        return(multiply(num1, num2))

    elif operator == '/':
        #print(num1, "/", num2, "=", divide(num1, num2))
        return(divide(num1, num2))










































































