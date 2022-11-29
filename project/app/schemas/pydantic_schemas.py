import datetime
from typing import Any

from pydantic import BaseModel, Field, validator
from pydantic.utils import GetterDict

from .custom_validators import curp_validator, rfc_validator, \
    codigo_postal_validator, fecha_nacimiento_validator, UserRole


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
    password: str = Field(..., min_length=4)


class UsuarioOutSchema(MyBaseSchema):
    nombre_usuario: str
    rol: UserRole
    created_at: datetime.datetime


class UsuarioModRoleSchema(MyBaseSchema):
    rol: UserRole


class EmpleadoSchema(MyBaseSchema):
    nombre: str = Field(..., min_length=2, max_length=50,
                        example='Samuel Gómez')
    curp: str = Field(..., example='GOBS971215HVZMLM04')
    rfc: str = Field(..., example='GOBS971215UH5')
    codigo_postal: str = Field(..., example='11490')

    # Validators
    _curp_validator = validator('curp', allow_reuse=True)(curp_validator)
    _rfc_validator = validator('rfc', allow_reuse=True)(rfc_validator)
    _codigo_postal_validator = validator(
        'codigo_postal', allow_reuse=True)(codigo_postal_validator)


class EmpleadoInSchema(EmpleadoSchema):
    fecha_nacimiento: str = Field(..., example='1997-12-15')

    # Validators
    _fecha_nacimiento_validator = validator(
        'fecha_nacimiento', allow_reuse=True)(fecha_nacimiento_validator)


class EmpleadoOutSchema(EmpleadoSchema):
    id: int
    fecha_nacimiento: datetime.date


class AuthenticationSchema(BaseModel):
    access_token: str
    token_type: str
