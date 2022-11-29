from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)
