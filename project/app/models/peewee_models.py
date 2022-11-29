from datetime import datetime

from peewee import Model, CharField, DateTimeField, \
    FixedCharField, DateField
from playhouse.postgres_ext import PostgresqlDatabase

import bcrypt

from ..config import DatabaseSettings

db_settings = DatabaseSettings()

psql_db = PostgresqlDatabase(
    db_settings.database_name,
    user=db_settings.database_user,
    password=db_settings.database_password,
    host=db_settings.database_host,
    port=db_settings.database_port,
)


class BaseModel(Model):
    class Meta:
        database = psql_db


class Usuario(BaseModel):
    nombre_usuario = CharField(max_length=50, unique=True)
    password = CharField()
    rol = CharField(max_length=13, default='operador')
    created_at = DateTimeField(default=datetime.now)

    @classmethod
    def authenticate(cls, nombre_usuario, password):
        user_authenticated = cls.get_or_none(
            cls.nombre_usuario == nombre_usuario)

        encoded_password = password.encode('utf-8')
        encoded_hashed_password = user_authenticated.password.encode('utf-8')
        if user_authenticated and bcrypt.checkpw(encoded_password, encoded_hashed_password):
            return user_authenticated

    @classmethod
    def create_password(cls, password):
        _bytes = password.encode('utf-8')
        return bcrypt.hashpw(_bytes, bcrypt.gensalt(6))


class Empleado(BaseModel):
    nombre = CharField(max_length=50)
    curp = FixedCharField(max_length=18)
    rfc = FixedCharField(max_length=13)
    codigo_postal = FixedCharField(max_length=5)
    fecha_nacimiento = DateField(formats=["%Y-%m-%d"])
