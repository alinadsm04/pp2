import os
# Task 1
# Write a Python program to list only directories, files and all directories, files in a specified path.

def task1():
    print("All folders in this path: ")
    for i in os.listdir(r"C:\Users\Алина\Desktop\pp2"):
        if os.path.isdir(os.path.join(r"C:\Users\Алина\Desktop\pp2", i)):
            print(i)
    print("\nAll files in this path: ")
    for i in os.listdir(r"C:\Users\Алина\Desktop\pp2"):
        if os.path.isfile(os.path.join(r"C:\Users\Алина\Desktop\pp2", i)):
            print(i)
    print("\nAll files and folders: ")
    for i in os.listdir(r"C:\Users\Алина\Desktop\pp2"):
        print(i)


# Task 2
# Write a Python program to check for access to a specified path. Test the existence, readability, 
# writability and executability of the specified path.

def task2():
    path = r"C:\Users\Алина\Desktop\pp2\hw6"
    path1 = os.access(path, os.F_OK)
    if(path1 == True):
        print("Your file exists")
    else:
        print("Your file does not exist")
    path2 = os.access(path, os.R_OK)
    if(path2 == True):
        print("I can read your file")
    else:
        print("I can not read your file")
    path3 = os.access(path, os.W_OK)
    if(path3 == True):
        print("I can write something in your file!")
    else:
        print("I can not write anything in your file")
    path4 = os.access(path, os.X_OK)
    if(path4 == True):
        print("I can execute your file")
    else:
        print("I can not execute your file")

# Task 3
# Write a Python program to test whether a given path exists or not. If the path exist find
# the filename and directory portion of the given path.

def task3():
    path = r"C:\Users\Алина\Desktop\pp2\hw6\builtin.py"
    if os.access(path, os.F_OK):
        print("Your path exists, trying to find the directory and filename")
        x = os.path.split(path) 
        print("The directory of the file:", x[0])
        print("The name of file:", x[1])
    else:
        print("Your path does not exist")

# Task 4
# Write a Python program to count the number of lines in a text file.
def task4():
    path = r"C:\Users\Алина\Desktop\pp2\hw6\text1.txt"
    f = open(path, "r")
    count = 0
    for i in f:
        if(i != "\n"):
            count += 1
    print("The amount of lines in this file is:", count)

# Task 5
# Write a Python program to write a list to a file.
def task5():
    path = r"C:\Users\Алина\Desktop\pp2\hw6\text1.txt"
    my_list = ["I am your friend", "John", "Do your best", 7, "Bye!"]

    f = open(path, "w")
    print("Let me write this list to your file:\n")
    print(my_list)
    for i in my_list:
        f.write(str(i) + " ")
    f.close()

    f = open(path, "r")
    print(f.read())

# Task 6
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def task6():
    path = r"C:\Users\Алина\Desktop\pp2\hw6\AtoZ"
    for i in range(65, 91):
        name = os.path.join(path, chr(i) +".txt")
        f = open(name, "a")
    for i in os.listdir(path):
        print(i)

# Task 7
# Write a Python program to copy the contents of a file to another file
def task7():
    path = r"C:\Users\Алина\Desktop\pp2\hw6\text1.txt"
    pathOfSecondfile = r"C:\Users\Алина\Desktop\pp2\hw6\text2.txt"
    # copying text.txt to text1.txt
    f = open(path, "r")
    f1 = open(pathOfSecondfile, "w")
    for i in f:
        f1.write(str(i))
    f1.close()
    f.close()

    f1 = open(pathOfSecondfile, "r")
    for i in f1:
        print(i)

# Task 8
# Write a Python program to delete file by specified path. Before deleting check for access 
# and whether a given path exists or not.

def task8():
    path = r"C:\Users\Алина\Desktop\pp2\hw6\text3.txt"
    if(os.access(path, os.F_OK)):
        print("Your path exist!\nI am deleting your file")
        os.remove(path)
        print("Deleting is succesful")
    else:
        print("Your path does not exist")