noNum = input("Enter a string: ")
def test1(str1):
    for i in str1:
        if i.isdigit():
            str1 = str1.replace(i, "")
    return str1

test1(noNum)