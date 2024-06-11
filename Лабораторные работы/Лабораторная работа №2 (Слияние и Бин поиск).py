import random
kol=(int(input('Сколько цифр будет в массиве: ')))
arr= random.sample(range(-100,100), kol)
print('Ваш массив: \n', arr)

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

MergeSort(arr)
print('Результат: \n', arr)

arr1= MergeSort(arr)
num=int(input('Число для поиска: '))

def BinSearch(arr,num):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    while num != arr[mid] and low <= high:
        if num > arr[mid]:
            low = mid + 1
        elif num < arr[mid]:
            high = mid - 1
        mid = (low + high) // 2
    if num == arr[mid]:
        print('Место в списке:', mid)
    else:
        print('Число не найдено')

BinSearch(arr,num)

