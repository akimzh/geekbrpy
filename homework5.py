#Задача 1

with open('task1.txt', 'w+', encoding='utf-8') as f:
	while True:
		str_ = str(input())
		if str_ == '':
			break
		f.write(str_+'\n')

#Задача 2

with open('task2.txt', 'r', encoding='utf-8') as f:
	for i, v in enumerate(f, 1):
		arr = v.strip().split(' ')
		print(f'Строка: {i}, Количество слов: {len(arr)}')

#Задача 3

with open('task3.txt', 'r', encoding='utf-8') as f:
	sum_ = 0
	count = 0
	for i in f:
		arr = i.strip().split(' ')
		sum_ += int(arr[1])
		count += 1
		if int(arr[1]) < 20000:
			print(arr[0])
	print('Средняя величина дохода сотрудников: ', sum_/count)

#Задача 4

with open('task4.txt', 'r', encoding='utf-8') as f:
	fi = open('task4e.txt', 'w', encoding='utf-8')
	for i in f:
		arr = i.split(' ')
		if arr[0] == 'One':
			arr[0] = 'Один'
		elif arr[0] == 'Two':
			arr[0] = 'Два'
		elif arr[0] == 'Three':
			arr[0] = 'Три'
		elif arr[0] == 'Four':
			arr[0] = 'Четыре'
		fi.write(' '.join(arr))
	fi.close()

#Задача 5

with open('task5.txt', 'w+', encoding='utf-8') as f:
	str_ = '2 4 5 10 2 3'
	f.write(str_)
	f.seek(0)
	arr = map(int, f.readline().split(' '))
	print('Результат:', sum(arr))

#Задача 6

import re

with open('task6.txt', 'r', encoding='utf-8') as f:
	dict_ ={}
	for i in f:
		dict_[re.findall(r'(\w+):', i)[0]] = sum(map(int, re.findall(r'\d+', i)))
	print(dict_)

#Задача 7

import json

with open('task7.txt', 'w+', encoding='utf-8') as f:
	while True:
		str_ = input("Введите данные о фирме,чтобы приостановить ввод введите 'stop' ") #Название, форма собственности, выручка, издержки
		if str_ == 'stop':
			break
		f.write(str_+'\n')
	avg_prof = 0
	count = 0
	dict_ = {}
	f.seek(0)
	for i in f:
		str_ = i.split(' ')
		profit = int(str_[2]) - int(str_[3])
		dict_[str_[0]] = profit
		if profit < 0:
			continue
		avg_prof += profit
		count += 1
	list_ = []
	list_.append(dict_)
	list_.append({'average_profit': avg_prof/count})
	with open('task7e.txt', 'w', encoding='utf-8') as fi:
		json.dump(list_, fi)