import boto3


def iga():
    testit()


def testit():
    person = {
        "name": "Joe",
        "guitars": [
            {
                "model": "Suhr",
                "cost": 3000
            },
            {
                "model": "Gibson",
                "cost": 2000
            },
            {
                "model": "Fender",
                "cost": 1000
            },
            {
                "model": "Suhr",
                "cost": 5000
            },
        ]
    }

    x = 1
    y = 2
    z = x
    z = 5

    #
    # print(id(x))
    # print(id(y))
    # print(id(z))
    # print(type(x))


    guitars = person['guitars']

    counter = 0
    cost = 0
    for g in guitars:
        if g['model'] == "Suhr":
            cost += g['cost']
            counter += 1

    print(f"There are {counter} Suhr guitars that total {cost}.")


    # print(person['guitars'][0])


def test():
    print('hello world marty was here')
    x = [1, 'a', 'this is a test', 1.1]
    my_bool = False

    if my_bool:
        print('true! ')
    else:
        print('no')

    d = {1: 'one',
         2: 'two',
         3: 'three'}
    my_variable_name = 'test'
    print(my_bool)


def test2(x, name):
    x[0] = 11111
    name = "bill"


if __name__ == '__main__':
    iga()
