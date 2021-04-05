from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

SECRET_KEY = '987rgsc9xm89ehckl'
SQLALCHEMY_DATABASE_URI = './sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Database Model
class UserModel (db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    id_no = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String, nullable=False, unique=True)
    amount = db.Column(db.String, nullable=False)
    acc_type = db.Column(db.String, nullable=False)

    def insert_record(self) -> None:
        db.session.add(self)
        db.session.commit()

# Account Type object for the strategy design
class AccountType(object):
    def __init__(self):
        super(AccountType, self).__init__()

    def determine_type(self, amount):
        amount = int(amount)
        if amount <= 5000:
            account_type = "Basic"
        elif 5001<= amount <= 15000:
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

# User object for the strategy design
class User(object):
    def __init__(self, fullname, id_no, phone, amount=None, acc_type = None):
        self.fullname = fullname
        self.id_no = id_no
        self.phone = phone
        self.amount = amount
        self.acc_type = acc_type
        self.account_type = AccountType()
        
        if len(acc_type) == 0 and len(amount) == 0:
            self.acc_type = 'Basic'
            self.default_amount_by_types()
        if len(amount) == 0 and acc_type != None:
            self.default_amount_by_types()
        if len(acc_type)== 0 and amount != None:
            self.determine_type()
        

    def determine_type(self):
        self.acc_type = self.account_type.determine_type(self.amount)
        return self.acc_type

    def default_amount_by_types(self):
        self.amount = self.account_type.default_amount_by_types(self.acc_type)
        return self.amount

    def __repr__(self):
        return f'{self.fullname} has registered a new account of type {self.acc_type} with amount {self.amount}'

# Ensure all tables are created in the database
@app.before_first_request
def create_tables():
    db.create_all()

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        users = UserModel.query.all()
        return render_template('index.html', users=users)
    if request.method == 'POST':
        fullname = request.form['fullname']
        id_no = request.form['id_no']
        phone = request.form['phone']
        amount = request.form['amount']
        acc_type = request.form['account_type']

        new_user_computed = User(fullname=fullname, id_no=id_no, phone=phone, amount=amount, acc_type=acc_type)

        new_user = UserModel(
            fullname=new_user_computed.fullname, 
            id_no=new_user_computed.id_no, 
            phone=new_user_computed.phone, 
            amount=new_user_computed.amount,
            acc_type=new_user_computed.acc_type
            )
        new_user.insert_record()

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)