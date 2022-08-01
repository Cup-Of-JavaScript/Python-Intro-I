def ex1():
    hello_world()


def ex2():

    array = [1, 2, 3]
    array_to_string(array)



def ex3():
    add_numbers()


def ex4():
    count_words()


def ex5():
    replace_period()


def ex6():
    slice_it()


def ex7():
    array = [2.00, 4.00, 4.00]
    calc_total(array)


def ex8():
    c_to_f()
    f_to_c()

def ex9():
    vowel_counter()



def ex10():
    calculator()


def ex11():
    sentence = "This is a test"
    diagonal_printer(sentence)


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

def hello_world():
    hello_world = range(3)
    for i in hello_world:
        print("Hello World from Python")


def array_to_string(array):
    x = ' '.join(str(s) for s in array)
    print(x)

def add_numbers():
    array = [1.0, 1.1, "1"]
    total = 0
    for x in array:
        total += float(x)
    print(total)


def count_words():
    sentence = input("Enter a sentence: ")
    count = len(sentence.split())
    print(f'There are {count} words')

def replace_period():
    sentence = "Test.  This is a test.  Testing."
    replace = sentence.replace(".", "!")
    print(replace)

def slice_it():
    array = ["this", "is", "another", "test"]
    r = "".join(s[:2] for s in array)
    print(r)

def calc_total(array):
    tax = "35%"
    total = 0
    for x in array:
        total += float(x)
        sum = "${:,.2f}".format((1+((float(tax[:2]))/100)) * total)
    print(sum)

def c_to_f():
    ce = input("Enter temperature in Celsius: ")
    c2f = (int(ce) * (9/5)) + 32
    print(f'{ce} is equals to {c2f} degrees Farenheit')


def f_to_c():
    fa= input("Enter temperature in Fahrenheit: ")
    f2c = (int(fa) - 32) * (5/9)
    print(f'{fa} degrees Fahrenheit is {f2c} degrees Celsius')


def vowel_counter():
    sentence = input("Enter a sentence: ")
    sentence.lower()
    counter = 0
    for x in sentence:
        if(x == 'a'or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
            counter = counter + 1
    print(f'Number of vowels: {counter}')

def calculator():
    answer1 = int(input("Enter first number: "))
    answer2 = int(input("Enter second number: "))
    answer3 = input("Choose operation: (+, *, /, -): ")

    if answer3 == '+':
        print(answer1 + answer2)

    if answer3 == '*':
        print(answer1 * answer2)

    if answer3 == '/':
        if answer2 == 0:
            print("Cannot divide by zero")
        else:
            print(answer1 / answer2)

    if answer3 == '-':
        print(answer1 - answer2)

def diagonal_printer(sentence):
    for i in range(len(sentence)):
        print(' '*i, sentence[i])






























def iga():
    car_list = [
        {
            "car_id": 1,
            "color": "red",
            "data": "Cost: 20000"
        },
        {
            "car_id": 2,
            "color": "red",
            "data": "Cost: 30000"
        },
        {
            "car_id": 3,
            "color": "yellow",
            "data": "Cost: 30000"
        }
    ]

    total = 0
    for x in car_list:
        if x['color'] == "red":
            total += int(x['data'][6:])
    print(total)