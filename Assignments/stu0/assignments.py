#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python I
#

import requests
import psycopg2
import boto3


def ex1():
    hello_world("3")


def ex2():
    array = [1, 2, 3]
    result = array_to_string(array)
    print(result)


def ex3():
    array = [1.0, 1.1, "1"]
    result = add_numbers(array)
    print(result)


def ex4():
    sentence = input("Enter sentence: ")
    num_words = count_words(sentence)
    print(num_words)


def ex5():
    sentence = "Test.  This is a test.  Testing."
    sentence2 = replace_period(sentence, "!")
    print(sentence2)


def ex6():
    array = ["this", "is", "another", "test"]
    r = slice_it(array)
    print(r)


def ex7():
    array = [2.00, 4.00, 4.00]
    tax = "10%"
    result = calc_total(array, tax)
    print(result)


def ex8():
    print(f_to_c(22))
    print(c_to_f(-6))


def ex9():
    sentence = "This is a test"
    num_vowels = vowel_counter(sentence)
    print(num_vowels)


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

def hello_world(num):
    num = int(num)
    for x in range(num):
        print("Hello World from Python!")


def array_to_string(array):
    retval = ""
    for i in array:
        retval += (str(i) + " ")
    return retval


def add_numbers(array):
    retval = 0.0
    for i in array:
        retval += float(i)
    return retval


def count_words(sentence):
    retval = 0
    word_array = sentence.split(" ")
    for word in word_array:
        if len(word) > 0:
            retval += 1
    return "Number of words: " + str(retval)


def replace_period(sentence, puncuation):
    retval = ""
    for letter in sentence:
        if letter == ".":
            retval += puncuation
        else:
            retval += letter
    return retval


def slice_it(array):
    retval = ""
    for w in array:
        retval += w[0:2]
    return retval


def calc_total(array, tax):
    retval = 0.0

    # Calculate total.
    for i in array:
        retval += i

    # Add taxes.
    tax_rate = float(tax[:-1])/100
    taxes = retval * tax_rate
    retval += taxes

    # Format output.
    retval = "${:,.2f}".format(retval)
    return retval;


def f_to_c(value):
    celsius = round((value-32) * (5/9))
    return f'{str(value)} degrees Fahrenheit is {celsius} degrees Celsius.'


def c_to_f(value):
    far = round(value * 9/5 + 32)
    return f'{str(value)} degrees Celsius is {far} degrees Fahrenheit.'


def vowel_counter(sentence):
    retval = 0
    vowels = "aeiou"
    for letter in sentence:
        if letter in vowels:
            retval += 1
    return f"Number of vowels: {retval}"
