def test2(list1):
    highNum = int(max(list1))
    lowNum = int(min(list1))
    return highNum - lowNum

test2(input("Enter a list of numbers separated by commas: ").split(","))