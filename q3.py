# 3. Write a python program to create a function that prints the even numbers from a
# given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1=[1,2,3,4,5,6,7,8,9]
def printEvenNum(l1):
    for i in l1:
        if(i%2==0):
            print(i,end=' ')

printEvenNum(l1)
