#Задача 1

import time

class TrafficLight:

	__color = 'красный'

	def running(self):
		print(self.__color)
		chck = self.check()
		next(chck)
		time.sleep(7)
		self.__color = 'белый' #Здесь нужно указать желтый
		next(chck)
		print(self.__color)
		time.sleep(2)
		self.__color = 'зеленый'
		next(chck)
		print(self.__color)
		time.sleep(5) #Продолжительность зеленого света 5 секунд

	def check(self):
		list_ =['красный', 'желтый', 'зеленый']
		for i in list_:
			if i == self.__color:
				pass
			else:
				raise SystemExit('Неправильный порядок режима светафора')
			yield i


tl = TrafficLight()
tl.running()

#Задача 2

class Road:

	def __init__(self, length, width):
		self._length = length
		self._width = width

	def mass(self):
		print('Масса асфальта покрытия всей дороги равна:',self._length*self._width*25*5)

rd = Road(20,5000)
rd.mass()

#Задача 3

class Worker:

	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": wage, "bonus": bonus}



class Position(Worker):

	def get_full_name(self):

		print('Полное имя сотрудника:', self.surname + ' ' + self.name)

	def get_total_income(self):

		print('Доход сотрудника с учетом премии:', self._income["wage"] + self._income["bonus"])


pos = Position('Иван', 'Пупкин', 'стажер программист', 10000, 2000)
pos.get_full_name()
pos.get_total_income()

#Задача 4

class Car:

	def __init__(self, speed, color, name, is_police):

		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = bool(is_police)

	def go(self):
		print('Машина поехала')

	def stop(self):
		print('Машина остановилась')

	def turn(self, direction):
		print(f'Машина повернула {direction}')

	def show_speed(self):
		print(f'Текущая скорость автомобиля {self.speed}')

class TownCar(Car):
	def show_speed(self):
		if self.speed > 60:
			print('Скорость автомобиля превышена')
		else:
			super().show_speed()

class SportCar(Car):
	pass

class WorkCar(Car):
	def show_speed(self):
		if self.speed > 40:
			print('Скорость автомобиля превышена')
		else:
			super().show_speed()

class PoliceCar(Car):
	pass


car = TownCar(100, 'желтый', 'Вольво', True)
car.go()
car.turn('налево')
car.show_speed()
car.stop()


car_ = WorkCar(20, 'синий', 'Опель', False)
car_.show_speed()

#Задача 5

class Stationery:

	def __init__(self, title):
		self.title = title

	def draw(self):
		print('Запуск отрисовки')

class Pen(Stationery):

	def draw(self):
		print('Отрисовка чернилами')

class Pencil(Stationery):
	
	def draw(self):
		print('Отрисовка графитовым грифелем')

class Handle(Stationery):
	
	def draw(self):
		print('Отрисовка краской')

pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()
handle_ = Stationery('маркер')
handle_.draw()




