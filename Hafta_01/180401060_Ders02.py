# Selection sort
def Selection(inList=[7, 6, 8, 9, 3, 2, 10, 5, 1]):
    n = len(inList)
    swaps, comparison = 0, 0
    for key in range(n):
        min = key
        for j in range(key+1, n):
            comparison += 1
            if inList[min] > inList[j]:
                min = j
        swaps += 1
        inList[key], inList[min] = inList[min], inList[key]
    return 'SelectionSorted List: {} \nComparison: {} \nSwap: {} '.format(
        inList, comparison, swaps)

# Bubble sort 
def Bubble(inList=[7, 6, 8, 9, 3, 2, 10, 5, 1]):
    n = len(inList)
    swaps, comparison = 0, 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparison += 1
            if inList[j] > inList[j+1]:
                swaps += 1
                inList[j], inList[j+1] = inList[j+1], inList[j]

    return 'BubbleSorted List: {} \nComparison: {} \nSwap: {} '.format(
        inList, comparison, swaps)
