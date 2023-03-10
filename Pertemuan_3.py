import math
def jumpSearch( arr , x , v ):
    step = math.sqrt(v)
    prev = 0
    for f in range(len(arr)):
        if type(arr[f]) == list:  
            o = jumpSearch(arr[int(f)],x,len(arr[int(f)]))
            if o == -1:
                arr[int(f)] = 'Ketemu'
                print()
            else:
                print(f'{x} Ditemukan di index {int(f)} kolom {o}')
                exit()
    while arr[int(min(step, v)-1)] < x:
                prev = step
                step += math.sqrt(v)
                if prev >= v:
                    return -1
    while arr[int(prev)] < x:        
                prev += 1
                if prev == min(step, v):
                    return -1
    if arr[int(prev)] == x:
            return int(prev)
    return -1
def fib(g):
    if g < 1:
        return 1
    elif g == 1 :
        return 1
    else:
        return fib(g-1) + fib(g-2)
def fibonaccisearch(arr,x):
    g1 = 0
    while fib(g1) < len(arr):
        g1 = g1 + 1
    offset = -1
    for b in range(len(arr)):
            if type(arr[b]) == list:
                w = fibonaccisearch(arr[b],x)
                if w == -1:
                    arr[b] = "Ketemu"
                else:
                    print(f'{x} Ditemukan di index {b} kolom {w}')
                    arr[b] = "Ketemu"
                    exit()
    while (fib(g1) > 1):
        i = min(offset + fib(g1-2), len(arr) - 1)
        if (x > arr[i]):
            g1 = g1-1
            offset = i
        elif (x < arr[i]):
            g1 = g1-2
        else:
            return i
    if (fib(g1-1) and arr[offset + 1] == x):
        return offset + 1
    return -1
def linearsearch(arr,x):
    for i in range(len(arr)):
        if type(arr[i]) == list:
            f = linearsearch(arr[i],x)
            if f == -1:
                return -1
            else:
                print(f'{x} ditemukan pada indeks {i} kolom {f}')
                exit()
        elif arr[i] == x:
            return i
    return -1
def Search1(arrA,t):
    r = fibonaccisearch(arrA,t)
    if r == -1:
        print(f'{t} Tidak ditemukan')
    else:
        print(f'{t} Ditemukan Di Index {r}')
def Search2(arrB,y):
    h = linearsearch(arrB,y)
    if h == -1:
        print(f'{y} Tidak ditemukan')
    else:
        print(f'{y} DItemukan Di Index {h}')
def search3(arrC,z,n1):
    m = jumpSearch(arrC,z,n1)
    if m == -1:
        print(f"{z} tidak ditemukan")
    else:
        print(f"{z} ditemukan di index {m}")

Data = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]

print(f'''
Arsel, Avivah, Daiva, Wahyu, Wibi
''')

n1 = len(Data)
while True:
    print('''
    1. Fibonacci Search
    2. Linear Search
    3. Jump Search
    ''')
    j = input("Masukan searching yang ingin anda gunakan: ")
    k = input("Masukan Data Yang Ingin Dicari: ")
    if j == '1':
        Search1(Data,k)
        break
    elif j == '2':
        Search2(Data,k)
        break
    elif j == "3":
        search3(Data,k,n1)
        break
    else:
        print("Masukan input dengan benar")