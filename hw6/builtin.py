import time
import math
# Task 1
# Write a Python program with builtin function to multiply all the numbers in a list
l = [1, 2, 3, 4]
def task1(list):
    product = 1
    for i in range(0, len(list)):
        product *= l[i]
    return product

# Task 2
# Write a Python program with builtin function that accepts a string and calculate
# the number of upper case letters and lower case letters
def task2():
    s = input()
    upperL = 0
    lowerL = 0
    for i in s:
        if(ord(i) >= 65 and ord(i) <= 90):
            upperL += 1
        elif(ord(i) >= 97 and ord(i) <= 122):
            lowerL += 1
    return f"Lower cases: {lowerL}\nUpper cases: {upperL}"

# Task 3
# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def task3():
    s = input()
    l = list(s)
    rl = reversed(l)
    s1 = ""
    for i in rl:
        s1 += i
    if(s1 == s):
        print(f"This string is palindrome, because {s} = {s1}")
    else:
        print(f"This string is not palindrome, because {s} != {s1}")

# Task 4
# Write a Python program that invoke square root function after specific milliseconds.
def task4():
    num = int(input())
    wait = int(input())
    time.sleep(wait / 1000)
    print(f"Square root of {num} after {wait} milliseconds is {math.sqrt(num)}")

# Task 5
# Write a Python program with builtin function that returns True if all elements of the tuple are true.
def task5():
    cnt = 0
    t = (0, True, 6, "Olzhas", 1, False)
    for i in t:
        if(bool(i) == False):
            return False
    return True
# i could use all()
print(task5())