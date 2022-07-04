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
    x = [1, 2, 3]
    result = array_to_string(x)
    print(result)





def ex3():
    print("TODO: Ex. 3...")


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

def hello_world(num):
    num = int(num)
    for x in range(num):
        print("Hello World from Python!")


def array_to_string(array):
    retval = ""
    for i in array:
        retval += (str(i) + " ")
    return retval
