from flask.ext.wtf import Form, TextField 
from flask.ext.wtf import Required, EqualTo

class RegisterForm(Form):
  link = TextField('RSS link', [Required()])
