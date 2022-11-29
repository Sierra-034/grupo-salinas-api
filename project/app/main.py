from fastapi import FastAPI, APIRouter, Depends, \
    HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.security import OAuth2PasswordRequestForm

from .models import create_tables, psql_db, Usuario
from .routers import usuarios_router, empleados_router
from .custom_errors import validation_exception_handler
from .common import create_access_token

app = FastAPI()


api_v1 = APIRouter(prefix='/api/v1')
api_v1.include_router(empleados_router)
api_v1.include_router(usuarios_router)


@api_v1.post('/auth')
async def auth(data: ... = Depends(OAuth2PasswordRequestForm)):
    user = Usuario.authenticate(data.username, data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Los campos [username] o [password] son incorrectos',
                            headers={'WWW-Authenticate': 'Bearer'}
                            )

    return {
        'access_token': create_access_token(user),
        'token_type': 'Bearer'
    }

app.include_router(api_v1)

validation_exception_handler = app.exception_handler(
    RequestValidationError)(validation_exception_handler)


@app.on_event('startup')
async def startup_event():
    psql_db.connect(reuse_if_open=True)
    create_tables()


@app.on_event('shutdown')
async def shutdown_event():
    psql_db.close()
