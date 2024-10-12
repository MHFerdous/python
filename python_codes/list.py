l1 = [1, 2, 40, 4]
print(l1)

l2 = [5, 6, 7, 8]
print(l2)

l2.append(9)
print(l2)

l1.extend(l2)
print(l1)

l1.insert(0, 10)
print(l1)

print(l1.index(2))

l1.remove(10)
print(l1)

l1.pop()
print(l1)

l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

print(type(l1))

listFruit = ['apple', 'banana', 'orange', 'mango']
print(listFruit)

listFruit = [item.capitalize() for item in listFruit]
print(listFruit)

listLen = [len(x) for x in listFruit]
print(listLen)
