
print(__name__)

list1 = [1, 'w', 4, True]

tuple1 = (1, 2, list1)

if list1[3]:
    print('there is true in list')
elif list1[4] - list1[1] > 0:
    print('there is great number in the list')
else:
    print('there is not true in the list')

birth = input('birth: ')
print(birth)

for element in list1:
    print(element)

for element in tuple1:
    print(element)