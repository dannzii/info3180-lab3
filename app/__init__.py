from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Dannzii'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'bd52eee4d7df35'
app.config['MAIL_PASSWORD'] = '5721143da6d507'

mail = Mail(app)
from app import views