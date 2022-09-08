# 4. Write a python program to create a function that checks whether a passed string is
# palindrome or not.

s=input("Enter a string: ")

def checkPalindrome(s):
    i=0
    j=len(s)-1
    while(j>=len(s)/2):
        if(s[i]==s[j]):
            i+=1
            j-=1
        else:
            return 0  
    else:
        return 1


print("{} is a Palindrome".format(s) if(checkPalindrome(s)==1) else "{} is not a palindrome".format(s))

