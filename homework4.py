#Задача 1

from sys import argv

prod_in_h, rate_per_h, bonus = map(int, argv[1:]) # prod_in_h - Выработка в часах, rate_per_h - Ставка в час, bonus - Премия

print('Заработанная плата сотрудника: ',(prod_in_h*rate_per_h)+bonus) 


#Задача 2

list_ = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

nlist_ = [list_[i] for i in range(1, len(list_)) if list_[i] > list_[i-1]]

print(nlist_)

#Задача 3

print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

#Задача 4

list_ = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


nlist_ = [x for x in list_ if list_.count(x) == 1]

print(nlist_)

#Задача 5

from functools import reduce

list_ = [i for i in range(100,1001) if i % 2 == 0]

print('Результат:',reduce(lambda x, y: x*y, list_))

#Задача 6

from itertools import count, cycle

#6.1

for i in count(3):
	print(i)
	if i == 10:
		break

#6.2

list_=['привет','Алекскей','ты','все','сможешь']

count = 0


for el in cycle(list_):
	print(el)
	count += 1
	if count == 2*len(list_): #Пусть завершится повторения элементов списка на 2 круге
		break

#Задача 7

def fact(n):
	gen = (i for i in range(1,n+1))
	for el in gen:
		yield el

factorial = 1
for el in fact(4):
	factorial *= el

print('Факториал равен:',factorial)

