list = [1,2,3,4,5]

def insertionSort(list):

    for i in range(1, len(list)):
        for j in range(i):

            if list[j]>list[i]:
                list[j],list[i] = list[i],list[j]
            # print(list)
    return list
i = insertionSort(list)
print(i)