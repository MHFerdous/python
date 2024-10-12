l1 = [1, 2, 3, 4, 5, 6]

n = input()
n = int(n)

flag = False
for item in l1:
    if n == item:
        print("Found")
        flag = True
        break

if flag is False:
    print("Not Found")
