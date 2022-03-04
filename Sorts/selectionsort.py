#https://www.youtube.com/watch?v=0-W8OEwLebQ&list=PLOmdoKois7_FK-ySGwHBkltzB11snW7KQ&index=5
a = [6, 9, 3, 0, 5]
N = len(a)
i = 0
while i < (N - 1):
    min = i
    for j in range(i + 1, N):
        if a[j] < a[min]:
            min = j
    b = a[i]
    a[i] = a[min]
    a[min] = b
    i = i + 1
print(a)
