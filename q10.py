# 10. Write a python program to create a function to check whether a string is an anagram
# or not.



def checkAnagram(s,s1):
    p=set(s)
    q=set(s1)
    if(p==q):
        return 1
    return 0

print("Anagram" if(checkAnagram(input("Enter a string: "),input("Enter a string: ")))==1  else "Not a anagram")     