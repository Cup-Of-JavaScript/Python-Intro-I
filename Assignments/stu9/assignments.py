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
def slice_it(array):
    slice = "".join(i[:2] for i in array)
    print(slice)


def replace_period(sentence):
    sen = sentence.replace(".", "!")
    print(sen)

def count_words(sentence):
    retval = len(sentence.split())
    return retval



def add_numbers(array):
    retval = 0
    for a in array:
        retval += float(a)
        print(retval)




def array_to_string(array):
    result = ' '.join(str(x) for x in array)
    print(result)




def hello_world(x):
    y = int(x)
    for y in range(y):
        print("Hello World from Python!")