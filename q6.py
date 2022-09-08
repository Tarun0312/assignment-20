# 6. Write a python program to create a function and print a list where the values are
# square of numbers between 1 and 30.

def printlistOfSquareof1to30():
    print([e**2 for e in range(1,31)],end=' ')

printlistOfSquareof1to30()    