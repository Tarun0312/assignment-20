# 5. Write a python program to create a function to find the Min of three numbers.

def min3numbers(a,b,c):
    return (a if(a<c) else c) if(a<b) else (b if(b<c) else c)


print(min3numbers(int(input("Enter 3 numbers to find minimum no: ")),int(input()),int(input())),"is a minimum number among three numbers")