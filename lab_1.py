#1
a = [1, 2, 3, 4, 5, 6, 7, 8]
def x(a):
    x1 = a[0]
    x2 = a[2]
    x3 = a[-2]
    return(x1, x2, x3)
print (x(a))

#2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = int(input())
def x(a):
    if N <= len(a):
        N1 = a[N] ** N
        return (N1)
    else:
        return (-1)
print (x(a))

#3
s = input("Введите строку: ")
b = input("Введите символ: ")
v = s.find(b, s.find(b)+1) #находит нименьший индекс и начиная с него ищет следующий наименьший
print(v)

#4
n = int(input("Введите число: "))
c = 0 #Вводим счетчик
if (n == 0): 
    print(1)

while (n % 10 == 0): #Пока остаток от деления равен нулю
    n //= 10         #Делим на цело и присваеваем новое значение
    c += 1           #Увеличиваем и присваеваем нвое значение счетчику
print(c)

#5
s = input("Введите строку: ")
n = s[::-1] #Перебор от начала до конца строки с шагом -1
print(n)

#6
def x(a):
    c = 0
    for i in range(len(a) - 1):
        if a[i] == a[i+1]:
            c += 1
    return (c == len(a) - 1)
t = x(a = [1])
        
print(t)

#7
a = ('ffffffffffffffff')
def x(a):
    c = 0
    b = 0
    n = 0
    for i in a:
       if (i.isupper()):
           c += 1
       if (i.isdigit()):
           b += 1
       if (i.islower()):
           n += 1
    if (c + b + n) >= 16 and (c + b + n) == len(a) and (c > 0) and (b > 0) and (n > 0):
        return (True)
    else:
        return (False)
print(x(a))

#8
a =[]
def x(a):
    g = []
    for i in a:
        if isinstance (i, list):
            g.extend(x(i))
        else:
            g.append(i)
    return(g)
print(x([1,2,3,[4,[5,[0]]]]))

#9
def x(a):
    ma_x = -1000000
    k = ""
    for i in list(a.keys()):
        if a[i] >= ma_x:
            ma_x = a[i]
            k = i
    return (k)
print(x({"k": 1,
         "k2": 2}))

#10
X = [1,3,2,3,2,4]
def garage(q):
    w = {} # создаем словарь
    for i in q:
        if i in w.keys():
            w[i] += 1 # если i уже есть в словаре, то прибавляем 1
        else:
            w[i] = 1 # если нет - приравниваем к 1
    return [e for e in q if w[e] > 1] # возвращаем е, которая бежит по списку, если в словаре этот элемент больше 1, т.е. встречается не один раз
2print(garage(X))
