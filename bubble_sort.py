list =  [8,7,5,4,1]
n = len(list)-1
def bubbleSort(list):
    i=0
    j=i+1
    while(i<len(list) and j<len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
            i+=1 
            j+=1  
        else:
            i+=1 
            j+=1
    return list
while(n>0):
    list = bubbleSort(list)
    n-=1
print(list)