"""Application entry point."""

from fastapi import FastAPI

from src.csv_to_xlsx.api.routes import router

app = FastAPI(title="File Converter API")

app.include_router(router)
