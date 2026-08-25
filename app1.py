# importar flask 
from flask import Flask

# crear una instancia de la aplicación Flask
app = Flask(__name__)

# definir las rutas de la aplicación 

@app.route('/')
def home():
    return '¡Hola, mundo! rutas con flask'

# ruta de productos
@app.route('/productos')
def productos():
    return '¡Bienvenido a la página de productos!'

# ruta de clientes 
@app.route('/clientes')
def clientes():
    return '¡Bienvenido a la página de clientes!'

# ruta de proveedores
@app.route('/proveedores')
def proveedores():
    return '¡Bienvenido a la página de proveedores!'

# ruta de facturacion
@app.route('/facturacion')
def facturacion():
    return '¡Bienvenido a la página de facturación!'

if __name__ == '__main__':
    app.run(debug=True)

    

