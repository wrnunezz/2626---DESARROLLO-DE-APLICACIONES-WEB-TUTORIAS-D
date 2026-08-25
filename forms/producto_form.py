from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField,IntegerField,SubmitField
from wtforms.validators import DataRequired, length, email

# clase producto

class Producto(FlaskForm):

    nombre=StringField('Nombre', validators=[DataRequired(),length(min=2,max=200,message='El nombre debe tener al menos 2 caracteres y maximo 200')])
    precio=DecimalField('Precio',validator=[DataRequired()])
    