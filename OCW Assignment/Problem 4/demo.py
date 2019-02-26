import string


def permute(a, l, r):
    if l == r:
        print(" ".join(str(x) for x in a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]


string = input("Enter the String : ")
n = len(string)
a = list(string)
permute(a, 0, n-1)


def permuantaion(a, l, r):
    if l == r:
        print(" ".join(str(x) for x in a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permuantaion(a, l+1, r)
            a[l], a[i] = a[i], a[l]


print("\n\nthis is the Sceond Function : \n")
permuantaion(a, 0, n-1)
