from flask_login import UserMixin


class Usuario(UserMixin):

    def __init__(self, id, nombre, email):
        self.id = str(id)
        self.nombre = nombre
        self.email = email