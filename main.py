"""Application entry point."""

from fastapi import FastAPI

from src.core.routes import router as core_router
from src.csv_to_json.api.routes import router as csv_to_json_router
from src.csv_to_xlsx.api.routes import router as csv_to_xlsx_router
from src.csv_to_xml.api.routes import router as csv_to_xml_router
from src.jpg_to_pdf.api.routes import router as jpg_to_pdf_router
from src.jpg_to_webp.api.routes import router as jpg_to_webp_router
from src.json_to_csv.api.routes import router as json_to_csv_router
from src.json_to_xlsx.api.routes import router as json_to_xlsx_router
from src.json_to_xml.api.routes import router as json_to_xml_router
from src.pdf_to_word.api.routes import router as pdf_to_word_router
from src.pdf_to_xlsx.api.routes import router as pdf_to_xlsx_router
from src.png_to_pdf.api.routes import router as png_to_pdf_router
from src.png_to_webp.api.routes import router as png_to_webp_router
from src.txt_to_csv.api.routes import router as txt_to_csv_router
from src.webp_to_jpg.api.routes import router as webp_to_jpg_router
from src.webp_to_png.api.routes import router as webp_to_png_router
from src.word_to_pdf.api.routes import router as word_to_pdf_router
from src.xlsx_to_csv.api.routes import router as xlsx_to_csv_router
from src.xlsx_to_json.api.routes import router as xlsx_to_json_router
from src.xlsx_to_pdf.api.routes import router as xlsx_to_pdf_router
from src.xlsx_to_xml.api.routes import router as xlsx_to_xml_router
from src.xml_to_csv.api.routes import router as xml_to_csv_router
from src.xml_to_json.api.routes import router as xml_to_json_router
from src.xml_to_xlsx.api.routes import router as xml_to_xlsx_router

app = FastAPI(title="File Converter API")

app.include_router(csv_to_json_router)
app.include_router(csv_to_xlsx_router)
app.include_router(csv_to_xml_router)
app.include_router(jpg_to_pdf_router)
app.include_router(jpg_to_webp_router)
app.include_router(json_to_csv_router)
app.include_router(json_to_xlsx_router)
app.include_router(json_to_xml_router)
app.include_router(pdf_to_word_router)
app.include_router(pdf_to_xlsx_router)
app.include_router(png_to_pdf_router)
app.include_router(png_to_webp_router)
app.include_router(txt_to_csv_router)
app.include_router(webp_to_jpg_router)
app.include_router(webp_to_png_router)
app.include_router(word_to_pdf_router)
app.include_router(xlsx_to_csv_router)
app.include_router(xlsx_to_json_router)
app.include_router(xlsx_to_pdf_router)
app.include_router(xlsx_to_xml_router)
app.include_router(xml_to_csv_router)
app.include_router(xml_to_json_router)
app.include_router(xml_to_xlsx_router)
app.include_router(core_router)
