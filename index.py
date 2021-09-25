from abc import ABC, abstractmethod

class IUser(ABC):
	@abstractmethod
	def getName(self):
		pass

class Administrator(IUser):
	name = str

	def __init__(self, name=None, role="Admin"):
		self.name = name
		pass

	def getName(self):
		return self.name

	def getRole(self):
		return self.name

class Customer(IUser):
	name = str

	def __init__(self, name=None):
		self.name = name

	def getName(self):
		return self.name

class IUserFactory(ABC):
	@abstractmethod
	def getModel(self):
		pass

class UserFactory(IUserFactory):
	model = IUser

	def __init__(self, data):
		try:
			if (data == "customer"):
				self.model = Customer(data)
			elif (data == "administrator"):
				self.model = Administrator(data)
			else:
				raise ValueError("Model not exist")
			pass
		except ValueError as ve:
			print(ve)
		pass

	def getModel(self) -> IUser:
		return self.model

if __name__ == '__main__':

	customer = UserFactory("customer").getModel()
	print("Hello, " +  customer.getName())

	administrator = UserFactory("administrator").getModel()
	print("Admin has role: " +  administrator.getRole())
