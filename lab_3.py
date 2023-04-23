#1
a = [1,2,3]
b = [4,5,6]
print(list(zip(a, b)))

#3
a = {}
for i in input().split():
	i = i.strip('.,!?:;-').lower()
	a[i] = a.get(i, 0) + 1 
print(min(a.items(), key=lambda x: (x[1], x[0]))[0])


#9
while True: print(eval(input()))
