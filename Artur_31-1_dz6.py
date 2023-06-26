def selection_sort(value):
    n = len(value)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if value[j] < value[min_idx]:
                min_idx = j
        value[i], value[min_idx] = value[min_idx], value[i]
    return value




def binary_search(Val, A):
    N = len(A)
    ResultOk = False
    first = 0
    Last = N - 1
    Pos = 0
    while True:

        if  first <= Last:

            Middle = (first + Last) // 2

            if Val == A[Middle]:
                first = Middle
                Last = first
                ResultOk = True
                Pos = Middle
            else:
                if Val > A[Middle]:
                    first = Middle + 1
                else:
                    Last = Middle - 1
        else:
            if ResultOk == True:
                 print(f'элемент найден индекс {Pos}')
            else:
                print(f'элемент не найден')

            break
binary_search(678,5000)