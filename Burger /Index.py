import datetime
import os
import sys


veg = {'Alooms': 49, 'Panner': 59, 'Mixveg': 99}
nonveg = {'Chickn': 129, 'Mutton': 149, 'C-Gril': 149, 'M-Gril': 199}
combos = [['Panner', 'Mutton', 179], ['Alooms', 'C-Gril', 179],
          ['Mixveg', 'Chickn', 199]]

user = "name"

now = datetime.datetime.now()

order = []  # [item name, item Price, item Count]
corder = []  # [item name 1, item name 2, item Price, item Count]

neworder = []


def optimizeBill():
    l = len(order)

    for ele in order:
        neworder.append(ele)

    # print(order)
    for i in range(0, l):
        #print('i = ', i)
        for j in range(i + 1, l):
            #print('j = ', j)
            for ele in combos:

                if(order[i][0] == ele[0] and order[j][0] == ele[1])or(order[i][0] == ele[1] and order[j][0] == ele[0]):
                    x = int(order[i][2])
                    y = int(order[j][2])

                    if(x > y):
                        rest = x - y
                        comb = x - rest

                        #order[i][2] = rest
                        corder.append([ele[0], ele[1], ele[2], comb])
                        neworder.remove(order[j])
                        neworder.remove(order[i])
                        neworder.append((ele[0], veg[ele[0]], rest))

                    else:
                        rest = y - x
                        comb = y - rest
                        #order[j][2] = rest

                        corder.append([ele[0], ele[1], ele[2], comb])
                        neworder.remove(order[i])
                        neworder.remove(order[j])
                        neworder.append((ele[1], nonveg[ele[1]], rest))
                l = len(order)

    order.clear()
    for ele in neworder:
        order.append(ele)


def printOrder():

    print("\n===================================================================")
    print("\t\t\tPRASAD Burger's Shop")
    print("===================================================================")
    print("Customer Name :    ", user)
    print('Bill Date     :    ', int(now.day),
          '-', int(now.month), '-', int(now.year))
    print("Bill Time     :    ", int(now.hour), ':',
          int(now.minute), ':', int(now.second))
    print('-------------------------------------------------------------------')
    print("Item\t\t\tPrice\t\tNo. of Items\tTotal Price")
    print('-------------------------------------------------------------------')
    sum = 0

    for ele in order:
        print(ele[0], '\t\t\t', ele[1], '\t\t  X  ',
              ele[2], '\t   ', int(ele[1]) * int(ele[2]))
        sum = sum + int(ele[1])*int(ele[2])

    print('\n')
    for ele in corder:
        print(ele[0], '+', ele[1], '\t', ele[2], '\t\t  X  ',
              ele[3], '\t   ', int(ele[2]) * int(ele[3]))
        sum = sum + int(ele[2]) * int(ele[3])

    print('-------------------------------------------------------------------')
    print('OverAll Total Price (INR) : ', '\t\t\t\t   ', sum, ' /-')
    print("===================================================================\n")


def nonVeg():
    for ele in nonveg.items():
        print(ele[0], ' \t= ', ele[1])
    choice = input("Type Item Name you Want : ")
    no = int(input('How Many Burger you want : '))
    order.append((choice, nonveg[choice], no))


def Veg():
    for ele in veg.items():
        print(ele[0], ' \t= ', ele[1])
    choice = input("Type Item Name you Want : ")
    no = int(input('How Many Burger you want : '))
    order.append((choice, veg[choice], no))


def Combos():
    x = 0
    for ele in combos:
        print(x, '= ', ele[0], ' + ', ele[1], '\t= ', ele[2])
        x += 1
    choice = int(input('Enter your Combo Choice No : '))
    no = int(input('How Many Combo you want : '))
    corder.append((str(combos[choice][0]),
                   str(combos[choice][1]), combos[choice][2], no))


list1 = [Veg, nonVeg, Combos]


def Menu():
    while True:
        print('1 : Veg Burger\t2: Non-Veg Burger \t3: Combos')
        choice = int(input('Enter the choice : '))
        if (choice > 3):
            break
        list1[choice-1]()
        os.system('clear')

    sys.stdout = open('out.txt', 'w+')

    printOrder()
    optimizeBill()
    print('\nOptimize bill------------\n')
    printOrder()


user = input("Enter the User Name : ")
Menu()

f = open('out.txt', 'r')
print(f.read())
f.close()
