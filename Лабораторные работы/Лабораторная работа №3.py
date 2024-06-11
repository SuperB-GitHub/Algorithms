from random import randint
import numpy as np 
import random

#Лабораторная 1 задание 1
def BubSort(a):
    for r in range (n-1):
        for i in range (n-1):
            if a[i]>a[i+1]:
                a[i], a[i+1]=a[i+1], a[i]

#Лабораторная 1 задание 2
def Vstavka(a):
    for i in range(1, n):
        d=a[i]
        j=i-1
        while j>=0 and d<a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=d

#Лабораторная 1 задание 3
def Vibor(a):
    for i in range (n-1):
            m=i
            j=i+1
            while j < n:
                if a[j]< a[m]:
                    m=j
                j+=1
            a[i], a[m]=a[m], a[i]
    
#Лабораторная 2 задание 1 
def MergeSort(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2
        left = arr[:mid] 
        right = arr[mid:]
        MergeSort(left) 
        MergeSort(right) 

        i = j = k = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1

        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1

        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1

            
#Лабораторная 2 задание 2 
def Xoare(g):
    srk=int(input('Введите кол-во строк:'))
    stl=int(input('Введите кол-во чисел:'))
    nu=np.random.randint(-100,100,size=(srk,stl))
    nu=np.transpose(nu)

    for b in range(0,stl):
        A=nu[b]

        def Xoaresort(A):
            if len(A) <= 1:
                return A
            else:
                q = random.choice(A)
                L = []
                C = []
                R = []
                for zn in A:
                    if zn < q:
                        L.append(zn) 
                    elif zn > q: 
                        R.append(zn) 
                    else: 
                        C.append(zn)
                return Xoaresort(L) + C + Xoaresort(R)

        A=Xoaresort(A)
        g.append(A)
    g=np.array(g)
    g.reshape(stl,srk)
    g=np.transpose(g)
    print(g)

#Лабораторная 2 задание 3 
def BinSearch(a,num):
    low = 0
    high = len(a) - 1
    mid = (low + high) // 2

    while num != a[mid] and low <= high:
        if num > a[mid]:
            low = mid + 1
        elif num < a[mid]:
            high = mid - 1
        mid = (low + high) // 2
    if num == a[mid]:
        print('Место в списке:', mid)
    else:
        print('Число не найдено')

#Лабораторная 3 задание 1 
def skobki():
    line=input() 
    stack=[] 
    GoodStr=True 

    for i in line: 
        if i in '([{': 
            stack.append(i) 
        elif i in ')]}': 
            if not stack: 
                GoodStr=False 
                break 
            up=stack.pop() 
            if (up=='(' and i==')') or (up=='[' and i==']') or (up=='{' and i=='}'):
                continue 
            else: GoodStr=False 
            break 
    if GoodStr==True and len(stack)==0:
        print('Правильная последовательность') 
    else: 
        print('Неправильная последовательность') 

#Лабораторная 3 задание 2 
def opn():
    a=[]
    action=input('').split() 
    for i in action:
        if i=='*':
            l=a.pop()
            j=a.pop()
            a.append(j*l)
        elif i=='/':
            l=a.pop()
            j=a.pop()
            a.append(j//l)
        elif i=='+':
            l=a.pop()
            j=a.pop()
            a.append(j+l)
        elif i=='-':
            l=a.pop()
            j=a.pop()
            a.append(j-l)
        else:
            a.append(float(i))

    print(a)


    
g=[]

a=[]
n=10
for i in range(n):
    a.append(randint(-99, 99))

z=True

while z==True:
    LabaNumber=int(input("Введите номер лабораторной работы 1-3, либо 0:"))
    ZadanNumber=int(input("Введите номер задания, либо 0:"))
    if LabaNumber==1 and ZadanNumber==1:
        BubSort(a)
        print(a)

    if LabaNumber==1 and ZadanNumber==2:
        Vstavka(a)
        print(a)

    if LabaNumber==1 and ZadanNumber==3:
        Vibor(a)
        print(a)

    if LabaNumber==2 and ZadanNumber==1:
        MergeSort(a)
        print(a)

    if LabaNumber==2 and ZadanNumber==2:
        Xoare(g)

    if LabaNumber==2 and ZadanNumber==3:
        BubSort(a)
        print(a)
        num = int(input('Введите необходимое число: '))
        BinSearch(a,num)

    if LabaNumber==3 and ZadanNumber==1:
        skobki()

    if LabaNumber==3 and ZadanNumber==2:
        opn()
    
    if LabaNumber==0:
        z=False
    
    