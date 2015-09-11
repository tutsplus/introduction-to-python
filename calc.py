
class Calc:

	def __init__(self):
		self.total = 0
		self.memory = []
		
	def add(self, a, b = None):
		if b is None:
			self.total += a
			self.memory.append(' + {0}'.format(a))
		else:
			self.total = a + b
			self.memory = []
			
	def subtract(self, a, b = None):
		if b is None:
			self.total -= a
			self.memory.append(' - {0}'.format(a))
		else:
			self.total = a - b
			self.memory = []
			
	def multiply(self, a, b = None):
		if b is None:
			self.total *= a
			self.memory.append(' * {0}'.format(a))
		else:
			self.total = a * b
			self.memory = []
			
	def divide(self, a, b = None):
		if b is None:
			self.total /= a
			self.memory.append(' / {0}'.format(a))
		else:
			self.total = a / b
			self.memory = []
			
	def remove_operation(self, op_number):
		if (op_number < 0) or (op_number > len(self.memory) - 1):
			return
		else:
			del self.memory[op_number]
			self.total = 0
			new_memory = self.memory
			self.memory = []
			
			for index in range(len(new_memory)):
				op = new_memory[index]
				values = op.split()
				first = values[0]
				second = values[1]
				if first == '+':
					self.add(int(second))
				elif first == '-':
					self.subtract(int(second))
				elif first == '*':
					self.multiply(int(second))
				else:
					self.divide(int(second))
			
	def show_memory(self):
		for index in range(len(self.memory)):
			print(index,":",self.memory[index])
		