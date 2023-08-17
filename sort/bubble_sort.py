import random

def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        print(li)
        if not exchange:
            return

li = [3,2,4,6,5,1,8,7,9]
print(li)
bubble_sort(li)
