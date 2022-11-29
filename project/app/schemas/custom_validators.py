import re
from enum import Enum


curp_regex = re.compile(
    r'^[A-Z]{1}[AEIOU]{1}[A-Z]{2}'
    r'[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])'
    r'[HM]{1}'
    r'(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)'
    r'[B-DF-HJ-NP-TV-Z]{3}'
    r'[0-9A-Z]{1}'
    r'[0-9]{1}$'
)

rfc_regex = re.compile(
    r'^[A-Z]{1}[AEIOU]{1}[A-Z]{2}'
    r'[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])'
    r'[A-Z]{2}'
    r'[0-9]{1}'
)

codigo_postal_regex = re.compile(r'[0-9]{5}')

fecha_nacimiento_regex = re.compile(
    r'[0-9]{4}-'
    r'(0[1-9]|1[0-2])-'
    r'(0[1-9]|1[0-9]|2[0-9]|3[0-1])'
)


class RoleType(Enum):
    ADMINISTRADOR = 'administrador'
    SUPERVISOR = 'supervisor'
    OPERADOR = 'operador'


def rol_must_be_one_of(value: str) -> str:
    if not isinstance(value, RoleType):
        raise ValueError(
            'El valor del campo rol debe ser uno de: \
            (administrador, supervisor, operador)'
        )

    return value


def create_formatter(regular_expression, field_name):
    def callback(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f'El campo {field_name} debe ser de tipo string')

        match = regular_expression.match(value.upper())
        if not match:
            raise ValueError(
                f'El campo {field_name} no cumple con el formato adecuado')

        return value

    return callback


curp_validator = create_formatter(curp_regex, '[curp]')
rfc_validator = create_formatter(rfc_regex, '[rfc]')
codigo_postal_validator = create_formatter(
    codigo_postal_regex, '[codigo_postal]')
fecha_nacimiento_validator = create_formatter(
    fecha_nacimiento_regex, '[fecha_nacimiento]')
