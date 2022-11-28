from fastapi import FastAPI, Depends

from .config import get_settings, Settings
from .models import create_tables, psql_db

app = FastAPI()


@app.on_event('startup')
async def startup_event():
    psql_db.connect(reuse_if_open=True)
    create_tables()


@app.on_event('shutdown')
async def shutdown_event():
    psql_db.close()


@app.get('/')
def index(settings: Settings = Depends(get_settings)):
    return {
        'Hello': 'world!',
        'environment': settings.environment,
        'testing': settings.testing,
    }
