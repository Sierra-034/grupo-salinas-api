import datetime
from typing import Any

from pydantic import BaseModel, Field
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if not getattr(self._obj, key, default):
            return default

        return getattr(self._obj, key, default)


class MyBaseSchema(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class UsuarioInSchema(BaseModel):
    nombre_usuario: str = Field(..., min_length=2, max_length=50)
    password: str = Field(..., min_length=4, max_length=50)


class UsuarioOutSchema(MyBaseSchema):
    nombre_usuario: str
    rol: str
    created_at: datetime.datetime


class UsuarioModRoleSchema(MyBaseSchema):
    role: str   # TODO Implement a custom type


class EmpleadoSchema(MyBaseSchema):
    nombre: str = Field(..., min_length=2, max_length=50)
    curp: str   # TODO Implement a custom type
    rfc: str    # TODO Implement a custom type
    codigo_postal: str  # TODO Implement a custom type
    fecha_nacimiento: datetime.date
