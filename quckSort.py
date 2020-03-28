#------------------#
#Quick Sort
#Author:Albert Bagdasarov
#Date: 24:11:19
#-------------------#
def quickSort(array):
    if len(array) < 2:
        return array
    else:
      pivot = array[0]
      less = [i for i in array[1:] if i <= pivot]
      greater = [i for i in array[1:] if i > pivot]

      return quickSort(less) + [pivot] + quickSort(greater)
print(quickSort([10,4,6,8,9,3]))
