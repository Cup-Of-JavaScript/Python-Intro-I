#
# File: assignments.py
# Date: 7/3/2022
# Desc: Intro Python I
#

import requests
import psycopg2
import boto3


def ex1():
    message = hello_world()
    print(message)

    # API
    r = requests.get('http://jsonplaceholder.typicode.com/users/1')
    print(r.json())

    # S3
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

    # Database
    con = psycopg2.connect(database='stu0', user='postgres', password='Ihgdp51505150!')
    cur = con.cursor()
    cur.execute('select * from book')
    r = cur.fetchall()  # fetchone()
    print(r)


def ex2():
    print("TODO: Ex. 2...")


def ex3():
    print("TODO: Ex. 1...")


def ex4():
    print("TODO: Ex. 1...")


def ex5():
    print("TODO: Ex. 1...")


def ex6():
    print("TODO: Ex. 1...")


def ex7():
    print("TODO: Ex. 1...")


def ex8():
    print("TODO: Ex. 1...")


def ex9():
    print("TODO: Ex. 1...")


def ex10():
    print("TODO: Ex. 1...")


def ex11():
    print("TODO: Ex. 1...")


def ex12():
    print("TODO: Ex. 1...")


def ex13():
    print("TODO: Ex. 1...")


def ex14():
    print("TODO: Ex. 1...")


def ex15():
    print("TODO: Ex. 1...")


#
# Place your functions here...
#

def hello_world():
    return "Hello World from Python."
