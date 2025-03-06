
def add(num1, num2):
    print("====Addition===")
    return num1 + num2


def multiply(num1, num2):
    print("====Multiplication===")
    return num1 * num2

def main():
    print("================Calculation=================")
    print("Perform Following Operations:\n\t1.Addition\n\t2.Multiplication\n")
    operation = int(input("Chooose your operation:"))
    print("Please Enter two numbers:")
    num1 = int(input("Enter Number 1:"))
    num2 = int(input("Enter Number 2:"))
    if operation == 1:
        print(f"Sum of {num1} and {num2} is {add(num1, num2)}")
    elif operation == 2:
        print(f"Multiplication of {num1} and {num2} is {multiply(num1, num2)}")
    else:
        print("Invalid Operation")

if __name__ == "__main__":
    main()

