from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email    = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=60)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
       
class SearchForm(FlaskForm):
    symbol    =   StringField('symbol', validators=[InputRequired(), Length(max=15)])  

class BuyForm(FlaskForm):
    symbol    =   StringField('symbol', validators=[InputRequired(), Length(max=15)])  
    shares    =   IntegerField('shares')

class SellForm(FlaskForm):
    symbol    =   SelectField('symbol', choices=[], validators=[InputRequired(), Length(max=15)])  
    shares    =   IntegerField('shares')