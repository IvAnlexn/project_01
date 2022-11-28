a = [7, 13, 5, 3, 9]
n = len(a)
print(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)


a = [7, 13, 5, 3, 9]
n = len(a)
print(a)
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        j += 1
    i += 1
print (a)