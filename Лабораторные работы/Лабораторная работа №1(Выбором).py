import time
a = []
for n in range(int(input('Введите нужную длину:'))):
    a.append(int(input('Введите нужные значение:')))
print('Ваша строка:',a)
print('Промежуточные результаты:')
start=time.time()

for i in range(len(a)):
        mini = i
        for j in range(i + 1, len(a)):
            if a[j] < a[mini]:
                mini = j
        a[mini], a[i] = a[i], a[mini]
        print(a)
        
end=time.time()
ttime=end-start
print('Ваша конечная строка:',a,'Время:',ttime)

