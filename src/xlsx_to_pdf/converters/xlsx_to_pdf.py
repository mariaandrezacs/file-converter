"""XLSX to PDF converter implementation."""

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from src.core.converter import Converter


class XlsxToPdfConverter(Converter):
    """Convert XLSX files into PDF format."""

    def convert(self, file, **options) -> dict:
        """Perform XLSX to PDF conversion."""
        try:
            df = pd.read_excel(file)
        except Exception as e:
            raise ValueError(f"Erro ao ler XLSX: {str(e)}") from e

        if df.empty:
            raise ValueError("O arquivo XLSX está vazio")

        output_file = "output.pdf"
        doc = SimpleDocTemplate(output_file, pagesize=letter)
        data = [df.columns.tolist()] + df.astype(str).values.tolist()

        table = Table(data)
        style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4A90E2")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ]
        )
        table.setStyle(style)

        doc.build([table])

        return {
            "output_file": output_file,
            "rows_processed": len(df),
            "columns": list(df.columns),
        }
