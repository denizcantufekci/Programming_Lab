"""
The functions My_f_1, My_f_2, and My_f_3 find the consecutive maximum total value in the array and assign it to the variable maxSum.

My_f_1, My_f_2 ve My_f_3 fonksiyonları dizi içindeki ardışık maksimum toplam değeri bulur ve bu değeri maxSum değişkenine atar.
"""

def my_f_1(inList=[4, -3, 5, -2, -1, 2, 6, -2]):
    maxSum = 0
    n = len(inList)
    for i in range(n):
        for j in range(i, n):
            t = 0
            for k in range(i, j):
                t = t + inList[k]
                if(t > maxSum):
                    maxSum = t
    return maxSum

def my_f_2(inList=[4, -3, 5, -2, -1, 2, 6, -2]):
    maxSum = 0
    n = len(inList)
    for i in range(n):
        t = 0
        for j in range(i, n):
            t = t + inList[j]
            if (t > maxSum):
                maxSum = t
    return maxSum

"""
My_f_3 function searches faster by dividing the array in half with each step.

My_f_3 fonksiyonu diziyi her adımda ikiye bölerek daha hızlı arama yapar.
"""
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))

def my_f_3(inList=[4, -3, 5, -2, -1, 2, 6, -2]): #More less control than other functions.
    n = len(inList)
    if (n == 1):
        return inList[0]
    left_i = 0
    left_j = n//2

    right_i = n//2
    right_j = n

    left_sum = my_f_3(inList[left_i:left_j])
    right_sum = my_f_3(inList[right_i:right_j])

    temp_left_sum = 0
    t = 0

    for i in range(left_j-1, left_i-1, -1):
        t = t + inList[i]
        if(t > temp_left_sum):
            temp_left_sum = t

    t = 0
    temp_right_sum = 0

    for i in range (right_i, right_j) :
        t = t + inList[i]
        if(t > temp_right_sum):
            temp_right_sum = t

    center_sum = temp_left_sum + temp_right_sum

    return max_of_three(left_sum, right_sum, center_sum)

#Some sort Functions

def InsertionSort(array=[4, 3, 2, 1]):
    n = len(array)
    for i in range(1,n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    return array

def ShellSort(array=[4, 3, 2, 1]):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j = j - gap
            array[j] = temp
        gap //= 2   # --> gap = gap // 2
    return array
