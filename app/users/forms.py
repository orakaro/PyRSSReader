from flask.ext.wtf import Form, SelectField, TextField, PasswordField, BooleanField, RecaptchaField
from flask.ext.wtf import Required, Email, EqualTo

class LoginForm(Form):
  email = TextField('Email', [Required(), Email()])
  password = PasswordField('Password', [Required()])

class RegisterForm(Form):
  name = TextField('Name', [Required()])
  email = TextField('Email', [Required(), Email()])
  password = PasswordField('Password', [Required()])
  confirm = PasswordField('Confirm Password', [
      Required(),
      EqualTo('password', message='Passwords must match')
      ])
  accept_tos = BooleanField('I accept the TOS', [Required()])
  gender = SelectField('Gender',choices = [('gender','Gender'),('male','Male'),('female','Female'),('other','Other'),('private','Private')] )
  recaptcha = RecaptchaField()
