a = [4,3,2,5,1]

for i in range(1,len(a)):
    for j in range(0,i):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]

print(a)
