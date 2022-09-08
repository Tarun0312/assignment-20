# 8. Write a python program to create a function that accepts a string and calculate the
# number of upper case letters and lower case letters.


def totalUppercaseLowercase(s):
    cu,cl=0,0
    for i in s:
        if('A'<=i<"Z"):
            cu+=1
        if("a"<=i<="z"):
            cl+=1
    print("Total Uppercase character={} and lowercase character={} in a given string".format(cu,cl)) 

totalUppercaseLowercase(input("Enter a string: "))