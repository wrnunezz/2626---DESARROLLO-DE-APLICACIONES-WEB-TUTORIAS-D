from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length


class ProductoForm(FlaskForm):

    nombre = StringField(
        'Nombre',
        validators=[
            DataRequired(),
            Length(min=2, max=200, message='El nombre debe tener al menos 2 caracteres y máximo 200' )
        ]
    )

    precio = DecimalField(
        'Precio',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Guardar')