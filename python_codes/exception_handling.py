try:
    fp = open("myFile.txt", "r")
    content = fp.read()
    fp.close()

except FileNotFoundError:
    print("Your file is not found")

print("***")

a = 1
b = 0
try:
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("***")
