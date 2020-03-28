#----------------------------#
 #Selection sort
 #Author:Albert Bagdasarov
 #21:10:19 21:36
#----------------------------#
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = indSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([112,-9,34,87,98]))
