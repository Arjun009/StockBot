from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForms(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)],render_kw={"placeholder": "User Name"})
    email= StringField('Email',validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    password= PasswordField('Password',validators=[DataRequired()],render_kw={"placeholder": "Password"})
    confirm_password= PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')],render_kw={"placeholder": "Confirm Password"})
    submit= SubmitField('Sign Up')


class LoginForms(FlaskForm):
    email= StringField('Email',validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    password= PasswordField('Password',validators=[DataRequired()],render_kw={"placeholder": "Password"})
    remember= BooleanField('Remember')
    submit= SubmitField('Log In')


class ForgetForms(FlaskForm):
    email= StringField('Email',validators=[DataRequired(), Email()],render_kw={"placeholder": "Email"})
    submit= SubmitField('Reset')    
    
    
class ResetForms(FlaskForm):
    password= PasswordField('Password',validators=[DataRequired()],render_kw={"placeholder": "Password"})
    confirm_password= PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')],render_kw={"placeholder": "Confirm Password"})
    submit= SubmitField('Change Password')


class MyForm(FlaskForm):
	stock = StringField('Stock', validators=[DataRequired(),
	Length(max=40)],render_kw={"placeholder": "Stock Name"})
    
    