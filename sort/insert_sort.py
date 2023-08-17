def insert_sort_(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] >= tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
    return li

li = [3, 5, 4, 8, 1, 6, 7]
new = insert_sort_(li)
print(new)