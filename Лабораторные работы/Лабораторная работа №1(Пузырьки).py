import time
a = []
for n in range(int(input('Введите нужную длину:'))):
    a.append(int(input('Введите нужные значение:')))
print('Ваша строка:',a)
print('Промежуточные результаты:')
start=time.time()
 
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(a)
end=time.time()
ttime=end-start
print('Ваша конечная строка:',a,'Время:',ttime)
