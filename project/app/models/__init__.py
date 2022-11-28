from .peewee_models import psql_db, Usuario, Empleado


def create_tables():
    with psql_db:
        psql_db.create_tables(models=[Usuario, Empleado])
