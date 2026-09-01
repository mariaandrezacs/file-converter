"""Application entry point."""

from fastapi import FastAPI

from src.csv_to_xlsx.api.routes import router as csv_to_xlsx_router
from src.json_to_csv.api.routes import router as json_to_csv_router
from src.xml_to_xlsx.api.routes import router as xml_to_xlsx_router

app = FastAPI(title="File Converter API")

app.include_router(csv_to_xlsx_router)
app.include_router(json_to_csv_router)
app.include_router(xml_to_xlsx_router)
