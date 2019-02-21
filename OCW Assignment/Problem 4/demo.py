import string

b = 0

def permute(a, l, r): 
    if l==r: 
        b += 1
        print (b+" ".join(str(x) for x in a))
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] # backtrack 
  
# Driver program to test the above function 
string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 
