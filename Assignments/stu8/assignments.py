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
    faren = 22
    celc = -6
    f_to_c(faren)
    c_to_f(celc)


def ex9():
    sentence = "This is a test"
    vowel_counter(sentence)


def ex10():
    result = calculator()
    print(result)

def ex11():
    sentence = "This is a test"
    diagonal_printer(sentence)


def ex12():

    stuff = "three three three two two one"
    word_histogram(stuff)
    # print(result)


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
    result = 0
    for x in array:
        result += float(x)
    print(result)


def count_words(sentence):
    num_words = len(sentence.split())
    print("Number of words: ", num_words)


def replace_period(sentence):
    sentence2 = sentence.replace(".", "!")
    print(sentence2)


def slice_it(array):
    r = "".join(a[:2] for a in array)
    print(r)


def calc_total(array, tax):
    result = 0
    for x in array:
        result += float(x)
    number = result * int(tax[:1])*.10
    dollar_number = "${:,.2f}".format(number + result)
    print(dollar_number)


def f_to_c (faren):

    result = int((faren - 32) * 5.0/9.0)
    print(f"{faren} degrees Fahrenheit is {result} degrees Celsius.")

def c_to_f (celc):

    result = int(9.0/5.0 * celc + 32)
    print(f"{celc} degrees Celsius is {result} degrees Fahrenheit.")


def vowel_counter (sentence):

    num_vowels=0
    for char in sentence:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels+1
    print(f"Number of vowels: {num_vowels}")


def calculator():
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y

    while True:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        choice = input("Enter operation (+, *, /, -): ")

        if choice == '+':
            print(add(num1, num2))

        elif choice == '*':
            print(multiply(num1, num2))

        elif choice == '/':
            print(divide(num1, num2))

        elif choice == '-':
            print(subtract(num1, num2))
        else:
            print("Invalid Input")

def diagonal_printer(sentence):

    words = str.split(sentence)
    for w in words:
        for i in range(len(w)):
            print(' '*i, w[i])

def word_histogram(input):
    dict = {
        'one' : 0,
        'two' : 0,
        'three': 0
    }
    stuff = input.split()
    for s in stuff:
        if s == 'one':
            dict['one'] = dict.get('one', 0) +1
        elif s == 'two':
            dict['two'] = dict.get('two', 0) +1
        elif s == 'three':
            dict['three'] = dict.get('three', 0) +1
    print(dict)