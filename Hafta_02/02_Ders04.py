#Insertion Sort
def InsertionSort(array=[4, 3, 2, 1]):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    return array
    
#Shell Sort
def ShellSort(array=[4, 3, 2, 1]):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j = j - gap
            array[j] = temp
        gap //= 2   # (gap = gap // 2)
    return array
