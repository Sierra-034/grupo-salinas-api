from datetime import datetime

from fastapi import APIRouter, Depends
from pytz import timezone

from ..models import Usuario
from ..schemas import UsuarioInSchema, UsuarioOutSchema, \
    RoleType
from ..dependencies import is_this_very_first_user

router = APIRouter(prefix='/users')


@router.post('', response_model=UsuarioOutSchema)
def create_user(usuario_in: UsuarioInSchema, is_very_first: ... = Depends(is_this_very_first_user)):
    mexico_city = timezone('America/Mexico_City')
    creation_date = datetime.now(tz=mexico_city)
    hashed_password = Usuario.create_password(usuario_in.password)

    usuario: Usuario
    if is_very_first:
        usuario = Usuario(
            **usuario_in.dict(), rol=RoleType.ADMINISTRADOR, create_at=creation_date)
    else:
        usuario = Usuario(**usuario_in.dict(),
                          created_at=datetime.now(tz=mexico_city))

    usuario.password = hashed_password
    usuario.save()
    return usuario
