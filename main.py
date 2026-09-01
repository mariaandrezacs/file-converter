"""Application entry point."""

from fastapi import FastAPI

from src.core.routes import router as core_router
from src.csv_to_json.api.routes import router as csv_to_json_router
from src.csv_to_xlsx.api.routes import router as csv_to_xlsx_router
from src.csv_to_xml.api.routes import router as csv_to_xml_router
from src.json_to_csv.api.routes import router as json_to_csv_router
from src.json_to_xlsx.api.routes import router as json_to_xlsx_router
from src.xlsx_to_csv.api.routes import router as xlsx_to_csv_router
from src.xlsx_to_json.api.routes import router as xlsx_to_json_router
from src.xml_to_csv.api.routes import router as xml_to_csv_router
from src.xml_to_xlsx.api.routes import router as xml_to_xlsx_router

app = FastAPI(title="File Converter API")

app.include_router(csv_to_json_router)
app.include_router(csv_to_xlsx_router)
app.include_router(csv_to_xml_router)
app.include_router(json_to_csv_router)
app.include_router(json_to_xlsx_router)
app.include_router(xlsx_to_csv_router)
app.include_router(xlsx_to_json_router)
app.include_router(xml_to_csv_router)
app.include_router(xml_to_xlsx_router)
app.include_router(core_router)
