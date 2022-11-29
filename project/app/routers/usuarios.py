from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, \
    status
from pytz import timezone

from ..models import Usuario
from ..schemas import UsuarioInSchema, UsuarioOutSchema, \
    UsuarioModRoleSchema
from ..dependencies import is_this_very_first_user
from ..dependencies import RoleChecker

router = APIRouter(prefix='/users')


@router.post('', response_model=UsuarioOutSchema)
def create_user(usuario_in: UsuarioInSchema, is_very_first: ... = Depends(is_this_very_first_user)):
    mexico_city = timezone('America/Mexico_City')
    creation_date = datetime.now(tz=mexico_city)
    hashed_password = Usuario.create_password(usuario_in.password)

    usuario: Usuario
    if is_very_first:
        usuario = Usuario(
            **usuario_in.dict(), rol='administrador', create_at=creation_date)
    else:
        usuario = Usuario(**usuario_in.dict(),
                          created_at=datetime.now(tz=mexico_city))

    usuario.password = hashed_password
    usuario.save()
    return usuario


@router.put(
    '/{user_name}', response_model=UsuarioOutSchema,
    dependencies=[Depends(RoleChecker(['administrador']))],)
def update_user(user_name: str, usuario_mod: UsuarioModRoleSchema):
    query = Usuario.update(**usuario_mod.dict()
                           ).where(Usuario.id == user_name).returning(Usuario)
    user_updated = query.execute()
    if len(user_updated) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Empleado con [id: {user_name}] no fué encontrado')

    return user_updated[0].__data__
