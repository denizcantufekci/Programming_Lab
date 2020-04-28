# UZEM:Hafta_04 derslerinde işlenen kod parçaları gerçeklendi.

def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)


def build_min_heap(array): 
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)
    

def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array


# UZEM:Hafta_04 derslerinde istenen kod parçaları gerçeklendi.

def insertItemToHeap(HeapArray, item):
    HeapArray.append(item)
    index = len(HeapArray)-1
    if index <= 0:
        return HeapArray
    parent = (index-1)//2
    while parent >= 0 and HeapArray[parent] > HeapArray[index]:
        HeapArray[parent], HeapArray[index] = HeapArray[index], HeapArray[parent]
        index = parent
        parent = (index-1)//2
    return HeapArray


def removeItemFrom(myArray):
    length = len(myArray)
    if length == 0:
        print("Heap is Empty")
        return myArray
    heapedArray = heapsort(myArray)
    heapedArray[0], heapedArray[-1] = heapedArray[-1], heapedArray[0]
    heapedArray.pop()
    build_min_heap(heapedArray)
    return heapedArray
