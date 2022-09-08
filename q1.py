# 1. Write a python program to create a function that takes a list and returns a new list
# with the original list's unique elements.


def uniqueEle(l1):
    l2=set(l1)
    return list(l2)

l=[12,34,12,3,4,34,56,12,4,5,5,5,6,3,3,3]

l3=uniqueEle(l)
print(l3)