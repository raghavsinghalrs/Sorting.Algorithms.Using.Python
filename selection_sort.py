list = [10,7,-5,12,-9]

def selectionSort(list):
    for i in range(len(list)):

        min = i

        for j in range(i+1, len(list)):

            if list[j] < list[min]:
                min=j
        
        list[i],list[min] = list[min],list[i]
    return list

s = selectionSort(list)
print(s)