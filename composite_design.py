class User(object):
	def __init__(self, fullname, id_no, phone, amount):
		self.fullname = fullname
		self.id_no = id_no
		self.phone = phone
		self.amount = amount


	def showDetails(self):
		# print("\t", end ="")
		print(self.fullname, '\n', self.id_no, '\n', self.phone, '\n', self.amount)


class AccountType(object):
	def __init__(self, acc_type):
		self.acc_type = acc_type
		self.children = []

	def add(self, child):
		self.children.append(child)

	def showDetails(self):
		for child in self.children:
			# print("\t", end ="")
			child.showDetails()


"""main method"""

if __name__ == "__main__":

	AccountType1 = AccountType('Basic')
	AccountType2 = AccountType('Advanced')
	AccountType3 = AccountType('Premium')

	User1 = User(fullname='Kelvin Kinuthia', id_no='12345678', phone='2547123456', amount=3000)
	User2 = User(fullname='David Letoo', id_no='12345678', phone='2547123456', amount=6000)


	AccountType1.add(User1)
	AccountType2.add(User2)
	print("------")
	AccountType1.showDetails()
	print("------")
	AccountType2.showDetails()

