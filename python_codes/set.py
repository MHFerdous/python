s = set()
print(s, type(s))

s.add(1)
print(s)

s1 = {1, 2, 4, 9}
s2 = {2, 4, 5, 8}

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

l1 = [1, 1, 2, 3, 2, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 9]
l1 = list(set(l1))
print(l1)

a = 'sdfsdjfksdjffks jsd fksjd'
print(a)

uniqueValue = {c for c in a}
print(uniqueValue)
