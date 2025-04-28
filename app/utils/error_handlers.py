from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import status

async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "No encontrado",
            "message": str(exc.detail) if hasattr(exc, 'detail') else "El recurso solicitado no existe."
        }
    )

async def validation_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Datos inválidos",
            "message": exc.errors()
        }
    )

async def internal_server_error_handler(request: Request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Error interno",
            "message": "Ocurrió un error inesperado. Por favor intenta más tarde."
        }
    )