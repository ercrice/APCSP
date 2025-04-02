def posts():
    num1 = input("Enter a number: ")
    num2 = input("Enter a bigger number: ")
    return print(list(range(int(num1), int(num2)+ 1)))

posts()