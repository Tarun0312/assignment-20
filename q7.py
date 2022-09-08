# 7. Write a python program to access a function inside a function.


def f2():
    print("Hello") 
def f1():
    f2()
    print("iNeuron")

f1()    