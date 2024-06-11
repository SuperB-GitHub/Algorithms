import random
import numpy as np 
g=[]
srk=int(input('Введите кол-во строк:'))
stl=int(input('Введите кол-во чисел:'))
n=np.random.randint(-100,100,size=(srk,stl))
print('Ваш массив:',n,sep='\n')
print()

n=np.transpose(n)
for b in range(0,stl):
    A=n[b]
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
