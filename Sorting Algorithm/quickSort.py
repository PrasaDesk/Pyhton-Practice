def partion(arr, start, end):
    pivot = arr[end]
    pIndex = (start)

    for i in range(start, end-2):
        if(arr[i] <= pivot):
            temp = arr[pIndex]
            arr[pIndex] = arr[i]
            arr[i] = temp

            pIndex = pIndex + 1

    temp = arr[pIndex]
    arr[pIndex] = arr[end]
    arr[end] = temp

    return pIndex


def quickSort(arr, start, end):

    if(start <= end):
        pIndex = partion(arr, start, end)
        quickSort(arr, start, pIndex - 1)
        quickSort(arr, pIndex + 1, end)
