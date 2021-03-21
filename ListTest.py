import requests

from functools import reduce

resp = requests.get('https://www.google.com')
print(resp.status_code)
# print(resp.text)


def fact(n):
    # there is potential stack issue as there would be too much tiers
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact1(n):
    # there is not stack issue
    return fact_fix(n, 1)


def fact_fix(num, product):
    if num == 1:
        return product
    return fact_fix(num-1, num*product)


def loop_list():
    L = []
    n =1
    while n <= 99:
        L.append(n)
        n = n + 2
    print('original ', L)
    L.pop(1)
    print('after pop ', L) 
    L.append('abc')
    print('append a str ', L)
    
    print(L)
#     splice
    print(L[:10:2])
    print(L[::5])
#     Iteration
    for i, v in enumerate(L):
        print(i, v)


def testlist():
    list1 = [1, 2, 3]
    print(list1[0:2])


def list_generator():
    l1 = [x * x for x in range(1, 11)]
    print(l1)
    l2 = [x * x for x in range(1, 11) if x % 2 == 0]
    print(l2)


def normalize(name):
    name = name.lower()
    first_char = name[:1]
    return first_char.upper() + name[1:]


def prod(element_list):
    def multiple(x, y):
        return x * y
    return reduce(multiple, L)


if __name__ == '__main__':
    # print(fact(5))
    # print(fact1(5))
    # loop_list()
    # testlist()
    list_generator()

    L1 = ['smith', 'JackSon', 'scoTT']
    L2 = list(map(normalize, L1))
    print(L2)

    L = [3, 4, 5, 6, 7, 8, 9]
    print(prod(L))
