#Задача 1

from itertools import zip_longest

class Matrix:

	def __init__(self, matr):

		self.isMatrix(matr)
		self.matr = matr
	
	def isMatrix(self, matr):
		if type(matr) is list:
			pass
		else:
			raise Exception('Это не матрица!')
		for i in matr:
			if type(i) is list:
				pass
			else:
				raise Exception('Это не матрица!')
			for j in i:
				if type(j) is int:
					pass
				else:
					raise Exception('Это не матрица!')

	def __str__(self):

		prMatr = []

		for i in self.matr:
			for j in i:
				prMatr.append(str(j) + ' ')
			if i == self.matr[-1]:
				break
			else:
				prMatr.append('\n')

		return ''.join(prMatr)

	def __add__(self, other):

		tempMatr = []

		for i, j in zip_longest(self.matr, other.matr, fillvalue = []):
			tempList = []
			for k, l in zip_longest(i,j, fillvalue = 0):
				tempList.append(k+l)
			tempMatr.append(tempList)
		
		return Matrix(tempMatr)


# mat2 = Matrix('sfdfs')
# mat3 = Matrix([3,2,1])
# mat4 = Matrix([['123',True, 5], [False, 2, 8]])
mat = Matrix([[1,2,3],[3,2,1],[5,6,7]])
mat1 = Matrix([[1,2,1], [2,3,-4]])
print(mat + mat1)

#Задача 2

from abc import ABC, abstractmethod

class Clothes(ABC):

	@abstractmethod
	def consumption(self):
		pass

class Coat(Clothes):
	
	def __init__(self, V):
		self.V = V

	@property
	def consumption(self):
		return f"Расход ткани на пальто составляет {self.V/6.5 + 0.5}"


class Suit(Clothes):

	def __init__(self, H):
		self.H = H

	@property
	def consumption(self):
		return f"Расход ткани на костюм составляет {2*self.H + 0.3}"


coat = Coat(6.5)
suit = Suit(1)
print(coat.consumption)
print(suit.consumption)

#Задача 3

class Cell:

	def __init__(self, count):

		self.count = count


	def __add__(self, other):
		return self.count + other.count

	def __sub__(self, other):
		if self.count - other.count > 0:
			pass
		else:
			raise Exception('Разность количества ячеек двух клеток меньше нуля')
		return self.count - other.count

	def __mul__(self, other):
		return self.count * other.count

	def __truediv__(self, other):
		return self.count // other.count

	def make_order(obj, amount = 5):
		str_ = ''
		for i in range(1, obj.count+1):
			str_ += '*'
			if i % amount == 0 and i != obj.count:
				str_ += '\n'
		return str_




c_1 = Cell(15)
c_2 = Cell(12)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)

print(Cell.make_order(c_2))
print(Cell.make_order(c_1))
