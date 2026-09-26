# importar flask 
from flask import Flask,render_template,request,redirect,url_for,flash
# importar psycopg2 para la conexion a la bd postgresql
from psycopg2.extras import RealDictCursor
from psycopg2.errors import RestrictViolation,ForeignKeyViolation
from Models.usuario import Usuario
from forms.login_form import LoginForm
from forms.usuario_form import UsuarioForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager,login_required, UserMixin, login_user, logout_user, logout_user, login_user,current_user


#from flask_sqlalchemy import  SQLAlchemy
from config import Config
from extensiones import db
from Models.producto import Producto

from Conexion.conexionp import obtener_conexion
#from Conexion.conexionp import obtener_conexion

# Importar formulario de productos Form . 

from forms.producto_form import ProductoForm
# crear una instancia de la aplicación Flask
app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

# =========================================================
# CONFIGURACIÓN DE FLASK-LOGIN
# =========================================================

login_manager = LoginManager()

login_manager.init_app(app)

# Si el usuario intenta entrar a una ruta protegida
# sin iniciar sesión, será enviado a /login
login_manager.login_view = 'login'

login_manager.login_message = 'Debe iniciar sesión para acceder al sistema.'

login_manager.login_message_category = 'warning'


@login_manager.user_loader
def load_user(user_id):

    conexion = obtener_conexion()

    cursor = conexion.cursor(
        cursor_factory=RealDictCursor
    )

    sql = """
        SELECT
            id,
            nombre,
            email
        FROM usuarios
        WHERE id = %s
    """

    cursor.execute(sql, (user_id,))

    datos_usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    if datos_usuario is None:
        return None

    return Usuario(
        datos_usuario['id'],
        datos_usuario['nombre'],
        datos_usuario['email']
    )



@app.route('/registro', methods=['GET', 'POST'])
def registro():

    form = UsuarioForm()

    if form.validate_on_submit():

        # Convertir la contraseña en HASH
        password_hash = generate_password_hash(
            form.password.data
        )

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO usuarios
            (nombre, email, password)
            VALUES (%s, %s, %s)
        """

        valores = (
            form.nombre.data,
            form.email.data,
            password_hash
        )

        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()

        flash(
            'Usuario registrado correctamente.',
            'success'
        )

        return redirect(url_for('registro'))

    return render_template(
        'registro.html',
        form=form
    )


# =========================================================
# LOGIN
# =========================================================

@app.route('/login', methods=['GET', 'POST'])
def login():

    # Si el usuario ya inició sesión
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()

    if form.validate_on_submit():

        conexion = obtener_conexion()

        cursor = conexion.cursor(
            cursor_factory=RealDictCursor
        )

        sql = """
            SELECT
                id,
                nombre,
                email,
                password
            FROM usuarios
            WHERE email = %s
        """

        cursor.execute(
            sql,
            (form.email.data,)
        )

        datos_usuario = cursor.fetchone()

        cursor.close()
        conexion.close()

        # Verificar que exista el usuario
        # y que la contraseña sea correcta
        if datos_usuario and check_password_hash(
            datos_usuario['password'],
            form.password.data
        ):

            usuario = Usuario(
                datos_usuario['id'],
                datos_usuario['nombre'],
                datos_usuario['email']
            )

            # Crear sesión
            login_user(usuario)

            flash(
                f'Bienvenido {usuario.nombre}.',
                'success'
            )

            return redirect(
                url_for('dashboard')
            )

        flash(
            'Correo electrónico o contraseña incorrectos.',
            'danger'
        )

    return render_template(
        'login.html',
        form=form
    )

# =========================================================
# CERRAR SESIÓN
# =========================================================

@app.route('/logout')
@login_required
def logout():

    logout_user()

    flash(
        'Sesión cerrada correctamente.',
        'success'
    )

    return redirect(
        url_for('login')
    )

@app.route('/dashboard')
@login_required
def dashboard():

    return render_template(
        'dashboard.html'
    )
# Clave secreta para el formulario Flkask wtf 
#app.config['SECRET_KEY'] = 'clave_secreta-ferreteria'

# Lista temporal de productos """
"""lista_productos = [
        {'id': 1, 'nombre': 'Martillo', 'precio': 10.99, 'stock': 50},
        {'id': 2, 'nombre': 'Taladro', 'precio': 19.99, 'stock': 0},
        {'id': 3, 'nombre': 'Destornillador', 'precio': 5.99, 'stock': 100}
    ]
"""



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
@login_required
def productos():
    # lista de bd 
    conexion = obtener_conexion()
    #cursor = conexion.cursor(dictionary=True)
    cursor=conexion.cursor(cursor_factory=RealDictCursor)

    sql=""" SELECT id_producto,nombre,precio_venta,stock  FROM producto where estado='true' """
    cursor.execute(sql)
    lista_productos=cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template(
        'productos.html',
        productos=lista_productos
    )


@app.route('/productos/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_producto():

    form = ProductoForm()

    if form.validate_on_submit():
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = "INSERT INTO producto (id_categoria,id_proveedor,nombre, precio_venta, stock) VALUES (%s,%s, %s, %s, %s)"
        valores = (1,1,form.nombre.data, form.precio.data, 0)

        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

        """ nuevo = Producto(
            nombre=form.nombre.data,
            precio=form.precio.data,
            stock=0)
        db.session.add(nuevo)
        db.session.commit()"""

        return redirect(url_for('productos'))

    return render_template(
        'formulario_producto.html',
        form=form
    )

# RUTA DE EDITAR PRODUCTOS
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):

    # creo el formulario
    form = ProductoForm()

    # cuando doy click en guardar
    if form.validate_on_submit():

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE producto
            SET nombre = %s,
                precio_venta = %s
            WHERE id_producto = %s
        """

        valores = (
            form.nombre.data,
            form.precio.data,
            id
        )

        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for('productos'))


    # buscar el producto en PostgreSQL
    conexion = obtener_conexion()

    cursor = conexion.cursor(
        cursor_factory=RealDictCursor
    )

    sql = """
        SELECT id_producto,
               nombre,
               precio_venta,
               stock
        FROM producto
        WHERE id_producto = %s
    """

    cursor.execute(sql, (id,))

    producto = cursor.fetchone()

    cursor.close()
    conexion.close()


    # verificar si existe
    if producto is None:
        return f'Producto con ID {id} no encontrado', 404


    # cargar los datos al formulario
    if request.method == 'GET':

        form.nombre.data = producto['nombre']
        form.precio.data = producto['precio_venta']


    return render_template(
        'formulario_producto.html',
        form=form
    )
   


# ruta de eliminar productos
@app.route('/productos/eliminar/<int:id>',methods=['POST'])
def eliminar_producto(id):

    print(f'Eliminando producto con id: {id}')

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:

        sql = """ DELETE FROM producto WHERE id_producto = %s """

        cursor.execute(sql, (id,))

        conexion.commit()

        print(f'Producto {id} eliminado correctamente')

    except RestrictViolation as e:

        conexion.rollback()

        print(f"Error al eliminar producto: {e}")

        flash (
            f'No se puede eliminar el producto con id {id} '
            f'porque está asociado a una factura.'
        )

    finally:

        cursor.close()
        conexion.close()

    return redirect(url_for('productos'))

# ruta de clientes
@app.route('/clientes')
@login_required
def clientes():

    # conexión con PostgreSQL
    conexion = obtener_conexion()

    # cursor tipo diccionario
    cursor = conexion.cursor(
        cursor_factory=RealDictCursor
    )

    # consulta SQL
    sql = """
        SELECT
            id_cliente,
            nombres,
            email
        FROM cliente
    """

    cursor.execute(sql)

    # obtener todos los clientes
    listado_clientes = cursor.fetchall()

    # cerrar cursor y conexión
    cursor.close()
    conexion.close()

    return render_template(
        'clientes.html',
        clientes=listado_clientes
    )
# ruta de editar clientes 
@app.route('/clientes/editar/<int:id>')
def editar_cliente(id):

    return f'EDitado el cliende id :{id}'

# ruta para eliminar clientes 
@app.route('/clientes/eliminar/<int:id>')
def eliminar_cliente(id):

    return f'Eli el cliende id :{id}'
# ruta de proveedores
# ruta de proveedores
@app.route('/proveedores')
@login_required
def proveedores():

    return render_template(
        'proveedores.html'
    )




if __name__ == '__main__':
    app.run(debug=True)

# ruta de facturación
@app.route('/facturacion')
@login_required
def facturacion():

    return render_template(
        'facturacion.html'
    )

if __name__ == '__main__':
    app.run(debug=True)
