# importar flask 
from flask import Flask,render_template,request,redirect,url_for

# crear una instancia de la aplicación Flask
app = Flask(__name__)

#definir las rutas de la aplicación
@app.route('/')
def home():
    return render_template('index.html')

# ruta de productos 
@app.route('/productos')
def productos():
    return render_template('productos.html')

# ruta de proveedores
@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html')

if __name__ == '__main__':
    app.run(debug=True)

