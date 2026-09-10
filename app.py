# importar flask 
from flask import Flask,render_template,request,redirect,url_for

#from flask_sqlalchemy import  SQLAlchemy
from config import Config
from extensiones import db
from Models.producto import Producto
from Conexion.conexion import obtener_conexion

# Importar formulario de productos Form 

from forms.producto_form import ProductoForm
# crear una instancia de la aplicación Flask
app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

# Clave secreta para el formulario Flkask wtf 
#app.config['SECRET_KEY'] = 'clave_secreta-ferreteria'

# Lista temporal de productos """
lista_productos = [
        {'id': 1, 'nombre': 'Martillo', 'precio': 10.99, 'stock': 50},
        {'id': 2, 'nombre': 'Taladro', 'precio': 19.99, 'stock': 0},
        {'id': 3, 'nombre': 'Destornillador', 'precio': 5.99, 'stock': 100}
    ]

# definir las rutas de la aplicación
@app.route('/')
def home():
    return render_template('index.html')

# ruta de productos
"""
@app.route('/productos')
def productos():
    # lista de bd 
    conexion = 
    lista_productos=Producto.query.all()
    return render_template(
        'productos.html',
        productos=lista_productos
    )
"""
@app.route('/productos')
def productos():
    # lista de bd 
    conexion = obtener_conexion()
    cursor=conexion.cursor(dictionary=True)

    sql=""" SELECT id_producto,nombre,precio_venta,stock  FROM producto """
    cursor.execute(sql)
    lista_productos=cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template(
        'productos.html',
        productos=lista_productos
    )


@app.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():

    form = ProductoForm()

    if form.validate_on_submit():

        nuevo = Producto(
            nombre=form.nombre.data,
            precio=form.precio.data,
            stock=0
        )


        db.session.add(nuevo)

        db.session.commit()

        return redirect(url_for('productos'))

    return render_template(
        'formulario_producto.html',
        form=form
    )

# RUTA DE EDITAR PRODUCTOS
@app.route('/productos/editar/<int:id>',methods= ['GET','POST'])
def editar_producto(id):

      # buscar ese producto por id 
      producto= next(( p for p in lista_productos if p['id']==id),None)
      print(producto)
   
      # creo el formulario 
      form=ProductoForm()
      #cuando doy click en guardar 
      if form.validate_on_submit():
          producto['nombre']=form.nombre.data
          producto['precio']=form.precio.data

          return redirect(url_for('productos'))
      #carga de los datos al formulario 
      if request.method=='GET':
          form.nombre.data=producto['nombre']
          form.precio.data=producto['precio']


      return render_template('formulario_producto.html', form=form)
   

# ruta de eliminar productos
@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
   

    # Aquí puedes implementar la lógica para eliminar un producto según su ID
    return f'Eliminar producto con ID: {id}'



# ruta de clientes
@app.route('/clientes')
def clientes():
# listado de clientes 
    listado_clientes = [
        {'id': 1, 'nombre': 'Juan Pérez', 'email': 'juap@gmail.com' },
        {'id':2, 'nombre': 'Pedro','email':'predro@gmail.com'}
        ]
         
    return render_template('clientes.html', clientes=listado_clientes)

# ruta de editar clientes 
@app.route('/clientes/editar/<int:id>')
def editar_cliente(id):

    return f'EDitado el cliende id :{id}'

# ruta para eliminar clientes 
@app.route('/clientes/eliminar/<int:id>')
def eliminar_cliente(id):

    return f'Eli el cliende id :{id}'
# ruta de proveedores
@app.route('/proveedores')
# listado de proveedores 


def proveedores():
    return render_template('proveedores.html')

if __name__ == '__main__':
    app.run(debug=True)
