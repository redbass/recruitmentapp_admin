from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField


class UserForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[validators.DataRequired()])

    type = StringField(
        'User Type',
        validators=[validators.DataRequired()])

    title = StringField(
        'Title',
        validators=[validators.DataRequired()])

    first_name = StringField(
        'First name',
        validators=[validators.DataRequired()])

    last_name = StringField(
        'Last name',
        validators=[validators.DataRequired()])

    password = PasswordField(
        'Password',
        validators=[validators.DataRequired()])

    def populate_form_from_core(self, user):
        self.username.data = user.get('_id', '')
        self.type.data = user.get('type', '')
        self.title.data = user.get('title', '')
        self.first_name.data = user.get('first_name', '')
        self.last_name.data = user.get('last_name', '')
        self.password.data = ""

    def create_job_core_from_form(self):
        return {
            "_id": self.data.get('username'),
            "type": self.data.get('type'),
            "title": self.data.get('title'),
            "first_name": self.data.get('first_name'),
            "last_name": self.data.get('last_name'),
            "password": self.data.get('password'),
        }
