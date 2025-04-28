from fastapi import FastAPI
from app.api.research import router as research_router
from app.api.investigations import router as investigations_router
from app.database.db import init_db

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.utils.error_handlers import not_found_handler, validation_exception_handler, internal_server_error_handler

def create_app():
    app = FastAPI(
        title="ResearchCitationAPI",
        version="1.0.0",
        description="API para generar investigaciones académicas rigurosas con citas verificables."
    )

    # Inicializar base de datos
    init_db()

    # Incluir routers
    app.include_router(research_router)
    app.include_router(investigations_router)

    # Manejo de errores personalizados
    app.add_exception_handler(StarletteHTTPException, not_found_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, internal_server_error_handler)

    return app

app = create_app()