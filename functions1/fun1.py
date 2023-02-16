<<<<<<< HEAD

#1
x = int(input())
def conv(x):
    print(x * 28.3495231)

conv(x)

#2
a = int(input())
def calc(a):
    print((5 / 9) * (a - 32))

calc(a) 

#3
numheads = int(input())
numlegs = int(input())
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits
    print(int(rabbits), int(chickens))

solve(numheads, numlegs)

#4
def is_prime(n):
    if(n == 1): return False
    if(n == 2): return True
    if(n % 2 == 0): return False

    p = int(n ** 0.5) + 1
    for i in range(3, p):
        if(n % i == 0):
            return False
    return True

def filter_prime(numbers):
    filtered_list = []
    for i in numbers:
        if(is_prime(i)):
            filtered_list.append(i)
    return filtered_list

#5
def next_permutation(a):
    n = len(a)
    i = 0
    j = 0
    for i in range (n - 2, -1, -1):
        if (a[i] < a[i + 1]):
            break
    if (i < 0):
        a.reverse()
    else:
        for j in range(n - 1, i, -1):
            if(a[j] > a[i]):
                break
        a[i], a[j] = a[j], a[i]

        st, end = i + 1, len(a)
        a[st:end] = a[st:end][::-1]

def prnt_nxt_prmttn(a):
    b = sorted(a, reverse = True)
    while a != b: 
        print (''.join(a)) 
        next_permutation(a)
    print(''.join(a))

a = [i for i in input()]
prnt_nxt_prmttn(a)

#6
def rev_words(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)
s = input()
print(rev_words(s))

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if(nums[i] == 3 and nums[i + 1] == 3):
            return True
    return False

#8

def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [0, 0, 7]:
            return True
    return False

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 

#9
def volume(r):
    result = (4 * 3.14 * r ** 3)/3
    print(result)

#10
def unique_list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

#11
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

#12
def hist(num):
    for i in num:
        print('*' * i)

#13
import random

def guess_the_num():
    name = input("Hello! What is your name?\n")
    print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
    number = random.randint(1, 20)
    guess = 0
    guesses = 0
    while guess != number:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
    print("Good job, {}! You guessed my number in {} guesses!".format(name, guesses))

guess_the_num()




=======

#1
x = int(input())
def conv(x):
    print(x * 28.3495231)

conv(x)

#2
a = int(input())
def calc(a):
    print((5 / 9) * (a - 32))

calc(a) 

#3
numheads = int(input())
numlegs = int(input())
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits
    print(int(rabbits), int(chickens))

solve(numheads, numlegs)

#4
def is_prime(n):
    if(n == 1): return False
    if(n == 2): return True
    if(n % 2 == 0): return False

    p = int(n ** 0.5) + 1
    for i in range(3, p):
        if(n % i == 0):
            return False
    return True

def filter_prime(numbers):
    filtered_list = []
    for i in numbers:
        if(is_prime(i)):
            filtered_list.append(i)
    return filtered_list

#5
def next_permutation(a):
    n = len(a)
    i = 0
    j = 0
    for i in range (n - 2, -1, -1):
        if (a[i] < a[i + 1]):
            break
    if (i < 0):
        a.reverse()
    else:
        for j in range(n - 1, i, -1):
            if(a[j] > a[i]):
                break
        a[i], a[j] = a[j], a[i]

        st, end = i + 1, len(a)
        a[st:end] = a[st:end][::-1]

def prnt_nxt_prmttn(a):
    b = sorted(a, reverse = True)
    while a != b: 
        print (''.join(a)) 
        next_permutation(a)
    print(''.join(a))

a = [i for i in input()]
prnt_nxt_prmttn(a)

#6
def rev_words(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)
s = input()
print(rev_words(s))

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if(nums[i] == 3 and nums[i + 1] == 3):
            return True
    return False

#8

def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [0, 0, 7]:
            return True
    return False

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 

#9
def volume(r):
    result = (4 * 3.14 * r ** 3)/3
    print(result)

#10
def unique_list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

#11
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

#12
def hist(num):
    for i in num:
        print('*' * i)

#13
import random

def guess_the_num():
    name = input("Hello! What is your name?\n")
    print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
    number = random.randint(1, 20)
    guess = 0
    guesses = 0
    while guess != number:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
    print("Good job, {}! You guessed my number in {} guesses!".format(name, guesses))

guess_the_num()




>>>>>>> 9b889b1b5de308f8ae28a0dee5840f2240d7f6a5
