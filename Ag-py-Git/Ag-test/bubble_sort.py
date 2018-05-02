

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


b = [2, 1, 3, 5, 4, 7, 6, 8, 1, 3]
print(b)
c = bubble_sort(b)
print(c)
