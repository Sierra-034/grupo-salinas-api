from datetime import datetime

from fastapi import APIRouter
from pytz import timezone

from ..models import Usuario
from ..schemas import UsuarioInSchema, UsuarioOutSchema

router = APIRouter(prefix='/users')


@router.post('', response_model=UsuarioOutSchema)
def create_user(usuario_in: UsuarioInSchema):
    mexico_city = timezone('America/Mexico_City')
    hashed_password = Usuario.create_password(usuario_in.password)
    usuario = Usuario(**usuario_in.dict(),
                      created_at=datetime.now(tz=mexico_city))

    usuario.password = hashed_password
    usuario.save()
    return usuario
