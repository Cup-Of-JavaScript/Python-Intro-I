#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python I
#


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

def hello_world(i):
    x = int(i)
    for i in range(x):
        print("Hello World from Python")

def array_to_string(array):
    my_string = ''
    for x in range(len(array)):
        my_string += ' '
        my_string += str(array[x])
    return my_string

def add_numbers(array):
    list = []
    for x in array:
        list.append(float(x))
    return sum(list)

def count_words(sentence):
    word_count = "Number of words: "
    return f'{word_count}{len(sentence.split())}'

def replace_period(sentence, x):
    punct_replacement = sentence.maketrans(".", "!")
    return sentence.translate(punct_replacement)

def slice_it(array):
    my_string = ''
    for x in range(len(array)):
        my_string += ''
        my_string += str(array[x][:2])
    return my_string

def calc_total(array, tax):
    x = int(tax[0:2])
    total = 0
    for i in array:
        total += i
    total = total + (total / x)
    total = "${:,.2f}".format(total)
    return total

def f_to_c(i):
    celsius = (i - 32) / 1.8
    return f'{i} {"degrees Fahrenheit is"} {round(celsius)} {"degrees Celsius."}'
def c_to_f(x):
    fahrenheit = round(x * 1.8) + 32
    return f'{x} {"degrees Celsius is"} {round(fahrenheit)} {"degrees Fahrenheit."}'

def vowel_counter(sentence):
    vowels = [each for each in sentence if each in "aeiouAEIOU"]
    return f'{"Number of vowels: "}{len(vowels)}'
