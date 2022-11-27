from fastapi import FastAPI, Depends
from .config import get_settings, Settings

app = FastAPI()


@app.get('/')
def index(settings: Settings = Depends(get_settings)):
    return {
        'Hola': 'mundo!',
        'environment': settings.environment,
        'testing': settings.testing,
    }
