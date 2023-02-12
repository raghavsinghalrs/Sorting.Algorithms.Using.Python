a = [7,9,13,12,6]

for i in range(0,len(a)-1):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
