
class AccountType(object):
    def __init__(self):
        super(AccountType, self).__init__()

    def determine_type(self, amount):
        if amount <= 5000:
            account_type = "Basic"
        elif 5001<= amount >= 15000:
            account_type = "Advanced"
        else:
            account_type = "Premium"
        return account_type

    def default_amount_by_types(self, account_type):
        if account_type == "Basic":
            amount = 5000
        elif account_type == "Advanced":
            amount = 15000
        elif account_type == "Premium":
            amount = 20000
        return amount


class User(object):
    def __init__(self, fullname, id_no, phone, amount=None, acc_type = None):
        self.fullname = fullname
        self.id_no = id_no
        self.phone = phone
        self.amount = amount
        self.acc_type = acc_type
        self.account_type = AccountType()
        
        if amount == None and acc_type != None:
            self.default_amount_by_types()
        if acc_type == None and amount != None:
            self.determine_type()


    def determine_type(self):
        self.acc_type = self.account_type.determine_type(self.amount)
        return self.acc_type

    def default_amount_by_types(self):
        self.amount = self.account_type.default_amount_by_types(self.acc_type)
        return self.amount

    def __repr__(self):
        return f'{self.fullname} has registered a new account of type {self.acc_type} with amount {self.amount}'


if __name__ == "__main__":
    usr_1 = User(fullname='Kelvin Kinuthia', id_no='12345678', phone='2547123456', amount=3000)
    usr_2 = User(fullname='David Letoo', id_no='12345678', phone='2547123456', acc_type='Advanced')

    print(usr_1)
    print(usr_2)
