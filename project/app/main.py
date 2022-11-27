from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()


@app.get('/')
def index(settings: Settings = Depends(get_settings)):
    return {
        'Hello': 'world!',
        'environment': settings.environment,
        'testing': settings.testing,
    }
