#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python I
#


def ex1():
    hello_world("3")


def ex2():
    array = [1, 2, 3]
    array_to_string(array)


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

def hello_world(a):
    b = int(a)
    for a in range(b):
        print("Hello World from Python!")


def array_to_string(array):
    result = ' '.join([str(i) for i in array])
    print(result)


def add_numbers(array):
    retval = 0
    for a in array:
        retval += float(a)
        print(retval)


def count_words(sentence):
    retval = len(sentence.split())
    return retval


def replace_period(sentence):
    retval = sentence.replace(".", "!")
    return retval
