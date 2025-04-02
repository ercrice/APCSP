def square(num1):
    return num1 ** 2

def greater(num1, num2):
    if num1 > num2:
        return print("The greater of the two numbers is" + " " + num1)
    else:
        return print("The greater of the two numbers is" + " " + num2)

def char(string, index):
    if index < 0 or index >= len(string):
        return "Index out of range. Please try again."
    else:
        return string[index]

def filtersort(list, num1, num2):
    sorted_list = sorted(list)
    
    filtered_list = [x for x in sorted_list if num1 <= x <= num2]
    
    return filtered_list

def commoninlist(list1, list2):
    common = [x for x in list1 if x in list2]
    if len(common) == 0:
        return "No common elements found."
    return common
    

