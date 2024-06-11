def LabaZadan1():
    def DeepSearch(graph, start, end):
        stack = [(start, [start])] # (вершина, путь от него) # vertex - вершина
        while stack:
            (vertex, path) = stack.pop()
            for next in set(graph[vertex]) - set(path): #set - позволяет работать со множеством строк
                if next == end:
                    yield path + [next] # yield - как return, но возвращает генератор различных путей, используется в итерации - подобие рекурсии, но не вызывает самого себя
                else:
                    stack.append((next, path + [next]))

   

    a = int(input('Введите количество вершин графа: '))  # создание квадратной матрицы
    mass = [[0] * a for i in range(a)]
    verstr = ''
    for i in range(a):
        verstr += str(i + 1) + '  ' 
    for i in range(len(mass)):
        for j in range(len(mass)):
            if i != j and i < j:
                print('Есть связь между вершиной ', i + 1, 'и', j + 1, '[д/н]? - ')
                res = str(input())
                if res == 'д':
                    mass[i][j] = 1
                    mass[j][i] = 1

    print('     Матрица     ')
    print('  ', verstr)
    for k in range(len(mass)):
        print(k + 1, mass[k])
   

    adj_list = [[j + 1 for j in range(len(mass[i])) if mass[i][j] != 0] for i in range(len(mass))] #словарь смежности, хранит в себе вершины, являющиеся соседями опред. вершины
    graph = {}
    print('---------------------------\n')
    print('     Граф     ')
    for i in range(a):
        graph[i + 1] = adj_list[i]
        print(i + 1, ':', graph[i + 1])
    print('---------------------------')
    
    start = int(input('Введите номер начальной вершины: '))
    end = int(input('Введите номер конечной вершины: '))
    print('---------------------------')
    print('     Пути:     ')
    list_paths = list(DeepSearch(graph, start, end)) #создание списка, в каждом элементе которого будет хранится список вершин определенного пути
    for i in range(len(list_paths)):
        print('Длина этого пути:', len(list_paths[i]) - 1, '|| Путь будет проходить:', list_paths[i])
    return ''

def LabaZadan2():
    import math

    def ShrtRd(Tabl, visited): #Выбор наименее короткой дороги
        minimum = -1
        maximum = math.inf  #Максимальное бесконечное значение
        for i, t in enumerate(Tabl): #enumerate - счетчик, который возвращает кортеж, содержащий пары ('счётчик', 'элемент') для элементов последовательности.
            if t < maximum and i not in visited:
                maximum = t
                minimum = i

        return minimum

    a = int(input('Введите количество вершин графа: '))
    mass = [[0] * a for i in range(a)]
    matrix = [[0] * a for i in range(a)]
    verhstr1 = ''

    for i in range(a):
        verhstr1 += str(i + 1) + '    '
    for i in range(len(matrix)):  # задание матрицы смежности
        for j in range(len(matrix)):
            if i != j and i < j:
                print('Введите расстояние между вершинами:', i + 1, 'и', j + 1,
                      'Если пути между этими вершинами нет, то введите 0')
                res = str(input())
                if res == '0':
                    matrix[i][j] = '*'
                    matrix[j][i] = '*'
                    mass[i][j] = math.inf
                    mass[j][i] = math.inf
                else:
                    matrix[i][j] = res
                    matrix[j][i] = res
                    mass[i][j] = int(res)
                    mass[j][i] = int(res)
            if i == j:
                matrix[i][j] = '0'
                mass[j][i] = 0
    print('-----------------------------------')
    print('     Матрица взвешанного графа     ')
    print('   ', verhstr1)
    for k in range(len(matrix)):
        print(k + 1, matrix[k])
    print('-----------------------------------')
    startpoint = int(input('Введите стартовую вершину: ')) - 1
    endpoint = int(input('Введите конечную вершину вершину: ')) - 1
    print('-----------------------------------')

    Tabl = [math.inf] * len(mass)  # последняя строка таблицы

    point = startpoint  # стартовая вершина
    visited = {point}  # множество просмотренных вершин
    Tabl[point] = 0  # нулевой вес для стартовой вершины
    optimal = [0] * len(mass)  # оптимальные связи между вершинами

    while point != -1:  # цикл, пока не просмотрим все вершины
        for j, dw in enumerate(mass[point]):  # перебираем все связанные вершины с вершиной point | enumerate - Выполняет роль счетчика элементов последовательности в циклах - типо функция генератор, формирующий совокупность таких путей с связанной вершиной
            if j not in visited:  # если вершина еще не была просмотрена, вторая проверка после генератора
                w = Tabl[point] + dw # w - вес
                if w < Tabl[j]:
                    Tabl[j] = w
                    optimal[j] = point  # связываем вершину j с вершиной point

        point = ShrtRd(Tabl, visited)  # выбираем следующий узел с наименьшим весом, ShrtRd - возвращает аргумент, т.е. вершину с мин.весом
        if point >= 0:  # выбрана очередная вершина
            visited.add(point)  # добавляем новую вершину в рассмотрение

    # формирование самого оптимального маршрута
    path = [endpoint]
    while endpoint != startpoint:
        endpoint = optimal[path[-1]]
        path.append(endpoint)
    result = []
    while path: result.append(path.pop() + 1)
    print('Самый короткий путь:', result)

    leen = 0
    for i in range(len(result) - 1):
        a1 = result[i] - 1
        a2 = result[i + 1] - 1
        leen += mass[a1][a2]
    print('Длина пути:', leen)
    return ''


znach=True
while znach==True:
    zadanie = int(input('Введите номер задания 4 лабораторной работы: '))
    if zadanie == 1:
        LabaZadan1()
    elif zadanie == 2:
        LabaZadan2()
    else:
        print('Задача не найдена!')