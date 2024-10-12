nameId = {1: 'A', 2: 'B', 3: 'C'}
print(nameId, type(nameId))

nameId[4] = 'D'
print(nameId)

print(nameId[1])

del nameId[4]
print(nameId)

for item, value in nameId.items():
    print(item, value)

print(nameId.items())

