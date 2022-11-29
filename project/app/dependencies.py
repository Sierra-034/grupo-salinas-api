from typing import List

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from .models import Usuario
from .common import decode_access_token

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth')


def is_this_very_first_user():
    num_users = Usuario.select().count()
    return num_users == 0


class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, token: str = Depends(oauth2_schema)):
        data = decode_access_token(token)
        if not data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Access token no válido',
            )

        if data['rol'] not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail='Operación no permitida')
