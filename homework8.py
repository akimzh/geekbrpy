#Задача 1

class Data:

	def __init__(self, data):
		self.data = data

	@staticmethod
	def checkData(obj):
		day, month, year = map(int, obj.data.split('-'))
		if day > 0 and day <= 31:
			pass
		else:
			raise Exception("Вы ввели не правильно день!")
		if month > 0 and month <= 12:
			pass
		else:
			raise Exception("Вы ввели не правильно месяц")
		if year > 0:
			pass
		else:
			raise Exception("До нашей эры")

	@classmethod
	def dataToInt(cls, obj):
		day, month, year = map(int, obj.data.split('-'))
		return cls(f'{day}-{month}-{year}')


data = Data('12-12-1994')
data_ = Data.dataToInt(data)
Data.checkData(data_)

data = Data('0-12-1994')
data_ = Data.dataToInt(data)
Data.checkData(data_)

#Задача 2

class Ex(Exception):
	def __init__(self, text):
		self.text = text

try:
	a = int(input('Введите числитель: '))
	b = int(input('Введите знаменатель: '))
	try:
		res = a / b
		print(res)
	except ZeroDivisionError:
		raise Ex('На нуль делить нельзя')
except Ex as err:
	print(err)

#Задача 3

class Ex(Exception):

	def __init__(self, text):
		self.text = text

list_ = []

while True:
	try:
		a = input('Введите число: ')
		if a == 'stop':
			break
		try:
			list_.append(int(a))
		except ValueError:
			raise Ex('Вы ввели не число!')
	except Ex as err:
		print(err)

print(list_)

#Задача 4, 5, 6

class WareHouse:

	dict_ = {}

	@classmethod
	def store(cls, obj):
		if type(obj.count) is int:
			pass
		else:
			raise Exception(f'Вы ввели не численный тип данных для {obj.title}') 
		if obj.title not in cls.dict_:
			cls.dict_[obj.title] = obj.count
		else:
			cls.dict_[obj.title] += obj.count

	@classmethod
	def to_take(cls, obj, companyName, count):
		if cls.dict_[obj.title] - count >=0:
			cls.dict_[obj.title] -= count
			return f"Мы передали {companyName} {obj.title} в количестве {count} "
		else:
			return "У нас нет подходящего количество товара на складе"


class OfficeEquipment:

	def __init__(self, title, maker, model):
		self.title = title
		self.maker = maker
		self.model = model

	def __str__(self):
		return f"{self.title} {self.maker} {self.model}"


class Printer(OfficeEquipment):

	def __init__(self,title,maker,model,count):
		super().__init__(title,maker,model)
		self.count = count
	
	def do(self):
		print('Печатает')

class Scanner(OfficeEquipment):
	
	def __init__(self,title,maker,model,count):
		super().__init__(title,maker,model)
		self.count = count
	
	def do(self):
		print('Сканирует')

class Xerox(OfficeEquipment):
	
	def __init__(self,title,maker,model,count):
		super().__init__(title,maker,model)
		self.count = count
	
	def do(self):
		print('Ксерокопирует')


pr = Printer('Принтер', 'HP', 'Laser 107wr', 100)
sc = Scanner('Сканер', 'Mustel', 'S 2400 Plus', 40)
sc_ = Scanner('Сканер', 'Mustel', 'S 2400 Plus', 40)
pr_ = Printer('Принтер', 'HP', 'Laser 107wr', 'lol')

print(pr)
pr.do()
WareHouse.store(pr)
WareHouse.store(sc)
WareHouse.store(sc_)
#WareHouse.store(pr_)
print(WareHouse.dict_)
print(WareHouse.to_take(sc_,'ТОО Морковка', 5))
print(WareHouse.dict_)

#Задача 7

class ComplexNumOperation:

	def __init__(self, num):

		self.num = complex(num)

	def __str__(self):
		return f"Результат = {self.num}"

	def __add__(self, other):
		return ComplexNumOperation(self.num + other.num)

	def __mul__(self, other):
		return ComplexNumOperation(self.num * other.num)


num1 = ComplexNumOperation('5-9j')
num2 = ComplexNumOperation('5-9j')
num3 = ComplexNumOperation('5-9j')
print(num1 + num2 + num3)
num4 = ComplexNumOperation('2-2j')
num5 = ComplexNumOperation('2-2j')
num6 = ComplexNumOperation('2')
print(num4 * num5 * num6)