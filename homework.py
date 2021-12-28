#Задача 1

a = 124
b = 'sdfsdfsd'
c = 4.3

print(a,b,c)

a = int(input("Введите число: "))
b = str(input("Введите строку: "))
с = float(input("Введите вещественное число: "))

print(a,b,c)

#Задача 2

sec = int(input("Введите количество секунд: "))

print(sec//3600,':', sec//60, ':', sec%60)

Задача 3

n = int(input("Введите число n: "))

print(n+int(str(n)+str(n)) + int(str(n) + str(n) + str(n)))

#Задача 4

num = int(input("Введите целое положительное число: "))

result = 0
while num > 0:
	last = num%10
	num = num//10
	dlastnum = num%10
	if dlastnum > last and dlastnum > result:
		result = dlastnum
	elif last > dlastnum and last > result:
		result = last



print(result)

#Задача 5

proceeds = float(input("Введите значение выручки фирмы: "))
costs = float(input("Введите значение издержек фирмы: "))

if proceeds > costs:
	print("Фирма работает с прибылью")
	print("Рентабельность выручки", (proceeds - costs)*100/proceeds, '%')
	count = int(input("Введите количество сотрудников: "))
	print("Прибыль фирмы в расчете на одного сотрудника: ", (proceeds - costs) / count)
elif costs > proceeds:
	print("Фирма работает с убытком")

#Задача 6

a = int(input())
b = int(input())
i = 1

while b > a - a*0.1 :
	print(str(i)+"-й"+" день:", round(a, 2))
	a = a*1.1
	i+=1\
