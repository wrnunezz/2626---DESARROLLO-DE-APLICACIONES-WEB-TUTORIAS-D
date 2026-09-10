import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = 'clave_secreta-ferreteria'

    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///' +
        os.path.join(BASE_DIR, 'data', 'ferreteria2.db')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
