def example(sequence):

    if(len(sequence) == 1):
        return [sequence]

    perms = example(sequence[1:])
    print("sequence = ", sequence)
    char = sequence[0]
    print(perms, char)
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])

    return result


input = input("Enter any string : ")
print(example(input))


''''
1 abc
2 bc
3 c  X


'''
