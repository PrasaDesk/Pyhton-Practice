# Selection Sort
# O(n ** 2) complexity


def selectionSort(arr, length):

    iMin = 0

    for i in range(length - 1):

        iMin = i

        # finding minimum Elemnet in array
        for j in range(i+1, length):

            if(arr[iMin] > arr[j]):
                iMin = j

        # Swap Min element
        temp = arr[i]
        arr[i] = arr[iMin]
        arr[iMin] = temp
