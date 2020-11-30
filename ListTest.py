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


def loopList():
    L = []
    n =1
    while n <= 99:
        L.append(n)
        n = n + 2
    print(L)


if __name__ == '__main__':
    print(fact(5))
    print(fact1(5))
    loopList()
