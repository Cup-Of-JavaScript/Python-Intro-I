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
    count_words(sentence)



def ex5():
    sentence = "Test.  This is a test.  Testing."
    replace_period(sentence)


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

#ex1:
def hello_world(a):
    b = int(a)
    for b in range(b):
        print("Hello World from Python!")


#ex2:
def array_to_string(array):
    retval = ' '.join(str(a) for a in array)
    print(retval)

#ex3:
def add_numbers(array):
    retval = 0
    for a in array:
        retval += float(a)
        print(retval)

#ex4
def count_words(sentence):
    num_words = sentence.count(" ")+1
    print("Number of words: ", num_words)


#ex5
def replace_period(sentence):
  sentence1 = sentence.replace(".", "!")
  print(sentence1)
