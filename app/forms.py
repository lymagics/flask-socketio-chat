from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Login Page form.
    
    :param username: user nickname field.
    :param room: room to enter field.
    :param submit: submit button.
    """
    username = StringField("Username", validators=[DataRequired()])
    room = StringField("Room", validators=[DataRequired()])
    submit = SubmitField("Join Room")
