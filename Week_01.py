def power_ord(a,b):   # Power Function is by the ordinary method.
    if b == 0:
        return 1
    if b == 1:
        return a
    m = 1
    for i in range(b):
        m *= a
    return m

def power_rcv(a,b):  # Power Function with recursive method.
    if b == 0:
        return 1
    if b == 1:
        return a
    if b > 1:
        if b % 2 == 0:
            return power_rcv(a*a, b/2)
        return power_rcv(a*a, b//2)*a
        #return power_rcv(a, b-1)*a

"""
The FindMaxRange function gives us the maximum range of elements
    between the elements in the array entered.
Max is the maximum total value in the array; i_1 and i_2 indicate the range values.

FindMaxRange fonksiyonu bize girilen dizideki elemanlar arasında,
    toplamları maksimum olan eleman aralığını verir.
Max, dizideki maksimum toplam değeridir; i_1 ve i_2 ise aralık değerlerini belirtir.
"""

def findMaxRange_i(inlist=[4, -3, 5, -2, -1, 2, 6, -2]):
    max = 0
    for i in range(len(inlist)):
        for j in range(i+1, len(inlist)):
            # print(i, j)
            t = 0
            for k in range(i,j+1):
                t = t + inlist[k]
            if t > max:
                max = t
                i_1, i_2 = i, j
    return max , i_1, i_2

def findMaxRange_ii(inlist=[4, -3, 5, -2, -1, 2, 6, -2]):   #Less control than first function.
    max = 0
    for i in range(len(inlist)):
        t = 0
        for j in range(i, len(inlist)):
            t = t + inlist[j]
            if t > max:
                max = t
                i_1, i_2 = i, j
    return max , i_1, i_2

#Some sort Functions

def Selection(inList=[7, 6, 8, 9, 3, 2, 10, 5, 1]):
    n = len(inList)
    swaps, comparison = 0, 0
    for key in range(n-1):
        for i in range(key+1,n):
            comparison += 1
            if inList[i] < inList[key]:
                swaps += 1
                inList[i], inList[key] = inList[key], inList[i]
    return 'SelectionSorted List: {} \nComparison: {} \nSwap: {} '.format(
        inList, comparison, swaps)

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
