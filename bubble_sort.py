list =  [10,7,5,6,-1]
n = len(list)-1
a=b=0
def bubbleSort(list,a,b):
    i=0
    j=i+1
    while (i<(len(list)-a) and j<(len(list)-b)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
            i+=1 
            j+=1  
        else:
            i+=1 
            j+=1
    return list
while(n>0):
    list = bubbleSort(list,a,b)
    a+=1
    b+=1
    n-=1
print(list)