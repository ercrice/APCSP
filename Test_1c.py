def test2(list1):
    highNum = int(max(list1))
    lowNum = int(min(list1))
    return highNum - lowNum

input1 = input("Enter a list of numbers separated by commas: ").split(",")
input2 = input("Enter another list of numbers separated by commas: ").split(",")

def test(list1, list2):
    range1 = test2(list1)
    range2 = test2(list2)
    if ((range1) > (range2)):
        print("The list, " + str(list1) + ", had the largest range of " + str(range1) + ".")
        return list1
    if ((range2) > (range1)):
        print("The list, " + str(list2) + ", had the largest range of " + str(range2) + ".")
        return list2
    
test(input1, input2)