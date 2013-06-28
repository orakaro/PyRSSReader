from flask.ext.wtf import Form, SelectField, TextField, PasswordField, BooleanField, RecaptchaField
from flask.ext.wtf import Required, Email, EqualTo

class RegisterForm(Form):
  facebook_id = TextField('Facebook ID', [Required()])
