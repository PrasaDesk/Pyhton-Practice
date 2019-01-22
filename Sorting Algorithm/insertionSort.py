# Insertion Sort
# O(n ** 2)


def insertionSort(arr, length):
    value = 0
    temp = 0

    # to control a loop and iterations
    for i in range(1, length):

        temp = i            # hole
        value = arr[i]      # value of the hole thats the minmum value

        '''  // While Loop explanation //
            if temp - 1 value is grater than value then we decrease temp - 1 and
            shift that hole to left side when temp in is 0 then loop stop means 
            value is minimum and we put this at first position 
        '''

        while(temp > 0 and arr[temp - 1] > value):

            # shifting large Number to right side of array
            arr[temp] = arr[temp - 1]

            # shifting hole to left side to put minimum value
            temp -= 1

        # putting minimum value to position
        arr[temp] = value
