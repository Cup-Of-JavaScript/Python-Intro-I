def ex1():
    hello_world()


def ex2():
    array_to_string()


def ex3():
    add_numbers()


def ex4():
    print("TODO: Ex. 4...")


def ex5():
    print("TODO: Ex. 5...")


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
def hello_world():
    hello_world = range(3)
    for i in hello_world:
        print("Hello World from Python")

def array_to_string():
    array = [1, 2, 3]
    x = ' '.join(str(s) for s in array)
    print(x)

def add_numbers():
    array = [1.0, 1.1, "1"]
    total = 0
    for x in array:
        total += float(x)
    print(total)

