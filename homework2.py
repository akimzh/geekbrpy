# Задача 1

list_ = ['abcd', 23, 3.2, [2,3, 'gssgs'], False]

for i in list_:
	print(type(i))

# Задача 2

list_ = []
index = -1
while True:
	i = input("Заполняем элементы списка,пока нет 'stop' ")
	if i == 'stop':
		break
	list_.append(int(i))
	index+=1
	if index % 2 != 0:
		list_[index-1], list_[index] = list_[index], list_[index-1]

print(list_)

# Задача 3

# решение через list

num_of_month = int(input("Введите месяц в виде целого числа: ")) 

list_ = ["Зима", "Весна", "Лето", "Осень"]

for i in range(0, len(list_)):
	if (num_of_month - 1)// 3 % 4 == i and num_of_month > 0:
		print(list_[i])

# решениие через dict

num_of_month = int(input("Введите месяц в виде целого числа: ")) 

dict_ = {"Зима": 0, "Весна": 1, "Лето": 2, "Осень": 3}

for i in dict_:
	if (num_of_month - 1) // 3 % 4 == dict_[i] and num_of_month > 0:
		print(i)

# Задача 4

str_ = str(input())

str_ = str_.capitalize().split(' ')

for i, elem in enumerate(str_, 1):
	print(i, elem[:10])

# Задача 5

my_list = [7, 5, 3, 3, 2]

while True:
	elem = input("Введите новый элемент рейтинга, чтобы остановить программу введите команду stop: ")
	if elem == 'stop':
		print(my_list)
		break
	elem = int(elem)
	for i in range(0,len(my_list)):

		elem = elem
		if elem > my_list[i]:
			my_list.insert(i, elem)
			break
		elif i==len(my_list)-1 and my_list[i] >= elem:
			my_list.append(elem)
	print(my_list)

#Задача 6

structure = []
number = 1

while True:
	doing_smth = str(input("Для перехода в аналитику программы напишите 'next', для завершения напишите 'stop', для последующего выполнения программы нажмите Enter: "))
	if doing_smth == 'stop':
		quit()
	elif doing_smth == 'next':
		break
	name = str(input("Введите название товара: "))
	price = int(input("Введите цену товара: "))
	count = int(input("Введите количество товара: "))
	unit = str(input("Введите единицу измерения: "))
	products = {"название": name, "цена": price, "количество": count, "ед": unit}
	tup = (number, products)
	structure.append(tup)
	print(structure)
	number+=1

analys = {}
list_name = []
list_price = []
list_count = []
list_unit = []
for i in structure:
	for j in i[1::]:
		for key, value in j.items():
			if key == 'название':
				if value not in list_name:
					list_name.append(value)
			elif key =='цена':
				if value not in list_price:
					list_price.append(value)
			elif key == 'количество':
				if value not in list_count:
					list_count.append(value)
			elif key == 'ед':
				if value not in list_unit:
					list_unit.append(value)

analys['название'] = list_name
analys['цена'] = list_price
analys['количество'] = list_count
analys['ед'] = list_unit
print(analys)
