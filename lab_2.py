#1
def fib_rec(n):
    if n in (1, 2):
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)
 
 
print(fib_rec(6))

#2
s = [1,2,3,4,5,6]
l = [4,5,6,7,8,9]

for i in s[:]:
    if i in l:
        s.remove(i)
        l.remove(i)

print(s, l)


#3
d = [1,2,2,2,2,4,4,5,5,5,5,6,6,6,6,6,6]
D = {}
t = int(input())
for i in d:
    D[i] = D.get(i, 0) + 1

f = {e: c for e, c in D.items() if c >= t}

print(f)


#4
a =[]
def x(a):
    g = []
    for i in a:
        if isinstance (i, list):
            g.append(sum(x(i)))
        else:
            g.append(i)
    return(g)
print(x([1,2,3,[4,[5,[0,7]]]]))

#5
e = [1,2,3,1,2,3,4,5,1,2,3,4,6,7]
exp: list[int] = []
max = []
for i in range(len(e)-1):
    if e[i] < e[i+1]:
        exp.append(e[i])
    else:
        exp.append(e[i])
        if len(exp) > len(max):
            max = exp
            exp = []
        if e[i] < e[i+1]:
            exp.append(e[i])
if e[-1] > e[-2]:
    exp.append(e[-1])
if len(exp) > len(max):
    max = exp
    exp = []
print(max)


#6
stroka = 'чмаф всех в чатике'
count = [i for i in range(len(stroka))]
print(''.join(stroka[i].upper() if (i % 2 != 0) else stroka[i] for i in count))

#7
n=int(input("Введите число: "))
k = n//2
if n%2 == 0:
    print('Ошибка. Введите нечетное число')
else:
    for i in range(k+1):
        if i == 0:
            print(" "*(k-i), '*', sep='', end='\n')
        else:
            j = list(range(1,n-1,2))[i-1]
            print(" "*(k-i), '*', " "*j, '*', sep='', end='\n')
    for i in range(k-1,-1,-1):
        if i > 0:
            j = list(range(n-k+(n-9)//2,-1,-2))[k-i-1]
            print(" "*(k-i), '*', " "*j, '*', sep='', end='\n')
        else:
            print(" "*(k-i), '*', sep='', end='\n')

#8
def matrix(num):
    mat = [[0 for i in range(num)] for j in range(num)]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == 0 or j == 0:
                mat[i][j] = 1
            else:
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j]," ", end='')
        print( sep=", ")
matrix(4)


#9
line = 'В этой 1 строке 4 всего 5 четыре числа 9'
words = line.split(' ')
product = 0
for word in words:
    try:
        value = int(word)
        product += value
    except:
        pass
print(product)

#10 Это я не поняла, что за зверь такой.
