# Bubble Sort
# O(n ** 2) complexity


def bubbleSort(arr, length):

    # controlling for loop
    for i in range(length):

        flag = 0

        # Comparing for loop actual logic
        for j in range(length - i - 1):

            # swaping elements
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

                flag = 1
        # if all element is sorted then we should break the loop
        if(flag == 0):
            break
