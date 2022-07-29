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
    array = [2.00, 4.00, 4.00]
    tax = "10%"
    calc_total(array, tax)


def ex8():
    cel = -6
    fah = 22
    c_to_f(cel)
    f_to_c(fah)


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

#ex6
def slice_it(array):
    r = "".join(i[:2] for i in array)
    print(r)

#ex7
def calc_total(array, tax):
    res = 0
    for i in array:
        res += float(i)
    number = res * int(tax[:1])*.10
    dollar_number = "${:,.2f}".format(number + res)
    print(dollar_number)


#ex8
def c_to_f(cel):
    r = int(9/5 * cel + 32)
    print(f"{cel} degrees Celsius is {r} degrees Fahrenheit")

def f_to_c(fah):
    result = int((fah - 32) * 5/9)
    print(f"{fah} degrees Fahrenheit is {result} degrees Celsius.")