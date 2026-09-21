from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):

    email = StringField(
        'Correo electrónico',
        validators=[
            DataRequired(),
            Email(message='Ingrese un correo electrónico válido')
        ]
    )

    password = PasswordField(
        'Contraseña',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Iniciar sesión')