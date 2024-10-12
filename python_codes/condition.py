n = input("Enter an integer value: ")
n = int(n)

if n >= 0 and n % 2 == 0:
    print(n, "is a positive & even number")
elif n >= 0 and n % 2 == 1:
    print(n, "is a positive & odd number")
elif n < 0 and n % 2 == 0:
    print(n, "is a negative & even number")
else:
    print(n, "is a negative & odd number")
