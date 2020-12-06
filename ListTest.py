import requests

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


def looplist():
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


def listgenerator():
    l1 = [x * x for x in range(1, 11)]
    print(l1)
    l2 = [x * x for x in range(1, 11) if x % 2 == 0]
    print(l2)


if __name__ == '__main__':
    # print(fact(5))
    # print(fact1(5))
    # looplist()
    # testlist()
    listgenerator()

