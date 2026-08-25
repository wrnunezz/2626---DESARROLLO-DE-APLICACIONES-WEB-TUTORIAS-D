# importar flask 
from flask import Flask,render_template,request,redirect,url_for

# crear una instancia de la aplicación Flask
app = Flask(__name__)

# definir las rutas de la aplicación
@app.route('/')
def home():
    return render_template('index.html')

# ruta de productos
@app.route('/productos')
def productos():


    lista_productos = [
        {'id': 1, 'nombre': 'Martillo', 'precio': 10.99, 'stock': 50},
        {'id': 2, 'nombre': 'Taladro', 'precio': 19.99, 'stock': 0},
        {'id': 3, 'nombre': 'Destornillador', 'precio': 5.99, 'stock': 100}
    ]
    return render_template('productos.html', productos=lista_productos)
# RUTA DE EDITAR PRODUCTOS
@app.route('/productos/editar/<int:id>')
def editar_producto(id):

    # Aquí puedes implementar la lógica para editar un producto según su ID
    return f'Editar producto con ID: {id}'

# ruta de eliminar productos
@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
    # Aquí puedes implementar la lógica para eliminar un producto según su ID
    return f'Eliminar producto con ID: {id}'



# ruta de clientes
@app.route('/clientes')
def clientes():

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
def proveedores():
    return render_template('proveedores.html')

if __name__ == '__main__':
    app.run(debug=True)
