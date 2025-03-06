# This program is used to multiply two numbers
def multipy(a,b):
    print("===============Multiplication=================")
    return a*b

print("Please Enter two numbers:")
a = int(input("Number 1:"))
b = int(input("Number 2:"))
result = multipy(a,b)
print(f"Multiplication of {a} and {b} is {result}")