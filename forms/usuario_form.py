from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class UsuarioForm(FlaskForm):

    nombre = StringField(
        'Nombre',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

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
            DataRequired(),
            Length(
                min=6,
                message='La contraseña debe tener mínimo 6 caracteres'
            )
        ]
    )

    confirmar_password = PasswordField(
        'Confirmar contraseña',
        validators=[
            DataRequired(),
            EqualTo(
                'password',
                message='Las contraseñas no coinciden'
            )
        ]
    )

    submit = SubmitField('Registrar usuario')