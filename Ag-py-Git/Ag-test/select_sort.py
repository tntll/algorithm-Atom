

def selecet_sort(a):
    num = len(a)
    for i in range(0, num-1):
        minindex = i
        for j in range(i+1, num):
            if a[j] < a[minindex]:
                minindex = j
        a[i], a[minindex] = a[minindex], a[i]
    return a


b = [2, 1, 3, 5, 4, 7, 6, 8, 1, 3]
print(b)
c = selecet_sort(b)

print(c)

min(b[0:2])
b.index(min(b[0:2]))
