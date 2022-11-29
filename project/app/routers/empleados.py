from typing import List

from fastapi import APIRouter, HTTPException, status

from ..schemas import EmpleadoInSchema, EmpleadoOutSchema
from ..models import Empleado

router = APIRouter(prefix='/empleados')


@router.post('', response_model=EmpleadoOutSchema)
async def create_empleado(empleado_in: EmpleadoInSchema):
    empleado = Empleado.create(**empleado_in.dict())
    return empleado


@router.get('', response_model=List[EmpleadoOutSchema])
async def get_empleados(page: int = 1, limit: int = 10):
    empleados = Empleado.select().paginate(page, limit)
    return [empleado for empleado in empleados]


@router.get('/{empleado_id}', response_model=EmpleadoOutSchema)
async def get_empleado(empleado_id: int):
    empleado = Empleado.get_or_none(Empleado.id == empleado_id)
    print(empleado)
    if not empleado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Empleado con [id: {empleado_id}] no fué encontrado')

    return empleado


@router.put('/{empleado_id}', response_model=EmpleadoOutSchema)
async def update_empleado(empleado_id: int, empleado_body: EmpleadoInSchema):
    query = Empleado.update(**empleado_body.dict()
                            ).where(Empleado.id == empleado_id).returning(Empleado)
    empleado_updated = query.execute()
    if len(empleado_updated) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Empleado con [id: {empleado_id}] no fué encontrado')

    return empleado_updated[0].__data__


@router.delete('/{empleado_id}', response_model=EmpleadoOutSchema)
async def delete_empleado(empleado_id: int):
    empleado = Empleado.get_or_none(Empleado.id == empleado_id)
    if not empleado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Empleado con [id: {empleado_id}] no fué encontrado')

    empleado.delete_instance()
    return empleado
