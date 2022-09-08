# 9. Write a python program to create a function to check whether a string is a pangram
# or not.


def checkPanagram(a):
    a.discard(' ')
    s={chr(i) for i in range(ord('a'),ord('{'))}
    if(a==s):
        return 1
    return 0

print("Panagram" if(checkPanagram(set(input("Enter a string: "))))==1 else "Not a panagram")


    