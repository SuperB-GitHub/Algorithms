import time
a = []
for n in range(int(input('Введите нужную длину:'))):
    a.append(int(input('Введите нужные значение:')))
print('Ваша строка:',a)
print('Промежуточные результаты:')
start=time.time()

for pos in range(len(a)):
        while pos > 0 and a[pos - 1] > a[pos]:
            a[pos] = a[pos - 1]
            pos = pos - 1
        a[pos] = a[pos]
        print(a)
end=time.time()
ttime=end-start
print('Ваша конечная строка:',a,'Время:',ttime)
