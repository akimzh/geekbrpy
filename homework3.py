#Задача 1

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите втоорое число: "))

def div(num1,num2):
	return num1/num2

try:
	print(div(num1,num2))
except ZeroDivisionError:
	print("Делить на нуль нельзя")

#Задача 2

def data(name, firstname, year_of_birth, city_of_res, email, phone_number):
	return print(f'{name} {firstname} {year_of_birth} {city_of_res} {email} {phone_number}')

data(name = 'Илья', firstname = 'Бобков', year_of_birth = 1992, city_of_res = 'Москва', email = 'example.geekbrains.ru', phone_number=79162034321)

#Задача 3

def my_func(num1, num2, num3):
	if num1 >= num2 and num3 >= num2:
		return num1 + num3
	elif num2 >= num1 and num3 >= num1:
		return num2 + num3
	elif num2 >= num3 and num1 >= num3:
		return num1 + num2

print(my_func(1,5,3))

#Задача 4

# 1 способ

def my_func(x,y):
	return x**y

print(my_func(0,0))

# 2 способ

def my_func(x,y):
	exp = 1
	if x == 0:
		print("По условию, если степень отрицательная x не равен нулю")
		return
	while y < 0:
		exp = 1/x * exp
		y+=1
	return exp

print(my_func(-2,-4))

#Задача 5

def sum_(str_, flag = True):
		result = 0
		for i in str_:
			try:
				result = result + int(i)
			except ValueError:
				if type(i) == str and i == str_[-1]:
					flag = False
					pass
				else:
					quit()
		return result, flag

bigSum = 0

while True:

	str_ = str(input("Введите строку чисел разделенных пробелом: "))

	str_ = str_.strip().split(' ')

	bigSum = bigSum + sum_(str_)[0]

	print(bigSum)

	if sum_(str_)[1] == False:
		break

#Задача 6

def int_func(str_):
	return str_.title()

print(int_func('text new realized'))
