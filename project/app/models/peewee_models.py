import datetime as dt

from peewee import Model, CharField, DateTimeField, \
    FixedCharField, DateField
from playhouse.postgres_ext import PostgresqlDatabase

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
    password = CharField(max_length=50)
    rol = CharField(max_length=13, default='operador')
    created_at = DateTimeField(default=dt.datetime.now)


class Empleado(BaseModel):
    nombre = CharField(max_length=50)
    curp = FixedCharField(max_length=18)
    rfc = FixedCharField(max_length=13)
    codigo_postal = FixedCharField(max_length=5)
    fecha_nacimiento = DateField(formats=["%Y-%m-%d"])
