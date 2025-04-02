def vowel(input1):
    list1 = ["a", "e", "i", "o", "u"]
    return [char for char in input1 if char in list1]

def vowels(input1, input2):
    vowels1 = vowel(input1)
    vowels2 = vowel(input2)
    return [char for char in vowels1 if char in vowels2]

print(vowels(input("Enter a string: "), input("Enter another string: ")))