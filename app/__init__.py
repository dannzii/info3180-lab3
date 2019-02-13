from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Dannzii'
app.config['MAIL_SERVER'] =  'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'dannzii'
app.config['MAIL_PASSWORD'] = 'dannzii@101'

mail = Mail(app)
from app import views