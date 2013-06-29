from flask.ext.wtf import Form, TextField, HiddenField
from flask.ext.wtf import Required, EqualTo

class RegisterForm(Form):
  link = TextField('RSS link', [Required()])


class DeleteForm(Form):
  feedName = HiddenField('FeedName', [Required()])
