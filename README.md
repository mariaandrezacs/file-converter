# File Converter

Projeto backend para **conversão de arquivos**, desenvolvido como um **sistema extensível de file-converter**, com foco em **arquitetura limpa**, **qualidade de código** e **boas práticas profissionais**.

Este projeto foi pensado como item de **portfólio**, demonstrando organização de código, testes, lint, automação, portabilidade e **capacidade de evolução para múltiplos conversores**.

---

## Visão do Sistema

O **File Converter** é o sistema principal.

Atualmente, ele possui os seguintes conversores implementados:

### Planilhas e Dados

* **CSV → JSON**
* **CSV → XLSX**
* **CSV → XML**
* **JSON → CSV**
* **JSON → XLSX**
* **JSON → XML**
* **JSON → YAML**
* **TXT → CSV**
* **XLSX → CSV**
* **XLSX → JSON**
* **XLSX → XML**
* **XLSX → PDF**
* **XML → CSV**
* **XML → JSON**
* **XML → XLSX**
* **YAML → JSON**

### Documentos

* **PDF → Word**
* **PDF → XLSX**
* **Word → PDF**

### Imagens

* **JPG → PDF**
* **JPG → WebP**
* **PNG → PDF**
* **PNG → WebP**
* **WebP → JPG**
* **WebP → PNG**

### Texto e Código

* **Base64 → Arquivo**
* **Arquivo → Base64**
* **HTML → Markdown**
* **Markdown → HTML**

A arquitetura foi desenhada para permitir a adição de novos conversores **sem alterar o core do sistema**.

---

## Arquitetura

O projeto segue uma separação clara de responsabilidades:

* **API**: camada HTTP (FastAPI)
* **Services**: orquestração e regras de aplicação
* **Converters**: lógica pura de conversão
* **Domain**: contratos e abstrações
* **Core**: rotas compartilhadas e contratos do sistema

```
src/
├── base64_to_file/         # Módulo Base64 → Arquivo
├── core/                   # Contratos e rotas compartilhadas
│   ├── converter.py
│   └── routes.py
├── csv_to_json/            # Módulo CSV → JSON
├── csv_to_xlsx/            # Módulo CSV → XLSX
├── csv_to_xml/             # Módulo CSV → XML
├── file_to_base64/         # Módulo Arquivo → Base64
├── html_to_markdown/       # Módulo HTML → Markdown
├── jpg_to_pdf/             # Módulo JPG → PDF
├── jpg_to_webp/            # Módulo JPG → WebP
├── json_to_csv/            # Módulo JSON → CSV
├── json_to_xlsx/           # Módulo JSON → XLSX
├── json_to_xml/            # Módulo JSON → XML
├── json_to_yaml/           # Módulo JSON → YAML
├── markdown_to_html/       # Módulo Markdown → HTML
├── pdf_to_word/            # Módulo PDF → Word
├── pdf_to_xlsx/            # Módulo PDF → XLSX
├── png_to_pdf/             # Módulo PNG → PDF
├── png_to_webp/            # Módulo PNG → WebP
├── txt_to_csv/             # Módulo TXT → CSV
├── webp_to_jpg/            # Módulo WebP → JPG
├── webp_to_png/            # Módulo WebP → PNG
├── word_to_pdf/            # Módulo Word → PDF
├── xlsx_to_csv/            # Módulo XLSX → CSV
├── xlsx_to_json/           # Módulo XLSX → JSON
├── xlsx_to_pdf/            # Módulo XLSX → PDF
├── xlsx_to_xml/            # Módulo XLSX → XML
├── xml_to_csv/             # Módulo XML → CSV
├── xml_to_json/            # Módulo XML → JSON
├── xml_to_xlsx/            # Módulo XML → XLSX
├── yaml_to_json/           # Módulo YAML → JSON
└── ...                     # Próximos conversores

tests/                      # Testes automatizados
main.py                     # Entry point da aplicação
```

---

## Tecnologias

* Python 3.10+
* FastAPI
* Uvicorn
* Pandas
* OpenPyXL
* python-multipart
* defusedxml
* PyYAML
* Markdown
* BeautifulSoup4
* pypdf
* python-docx
* ReportLab
* Pillow
* Pytest
* Ruff / Black / Pylint
* Docker
* GitHub Actions (CI)

---

## Executando localmente

### 1. Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install -e .[dev]
```

### 3. Subir a aplicação

```bash
uvicorn main:app --reload
```

Acesse:

```
http://localhost:8000/docs
```

---

## Executando com Docker

```bash
docker build -t file-converter .
docker run -p 8000:8000 file-converter
```

---

## Endpoints

Cada conversor expõe um endpoint específico no padrão:

```
POST /convert/{source}-to-{target}
```

Exemplos:

* `POST /convert/csv-to-xlsx`
* `POST /convert/json-to-csv`
* `POST /convert/xml-to-json`
* `POST /convert/yaml-to-json`
* `POST /convert/json-to-yaml`
* `POST /convert/xlsx-to-pdf`
* `POST /convert/word-to-pdf`
* `POST /convert/jpg-to-pdf`
* `POST /convert/webp-to-jpg`
* `POST /convert/markdown-to-html`
* `POST /convert/html-to-markdown`
* `POST /convert/file-to-base64`
* `POST /convert/base64-to-file`

Além disso, o sistema disponibiliza:

* `GET /download/{filename}` — download do arquivo gerado anteriormente

---

## Testes

```bash
pytest
```

---

## Qualidade de código

### Lint

```bash
ruff check .
```

### Formatação

```bash
black .
```

### Pre-commit

```bash
pre-commit install
```

---

## Decisões arquiteturais

* **File Converter** tratado como sistema central
* cada conversão implementa um contrato comum definido em `src/core/converter.py`
* conversores isolados da camada HTTP
* arquitetura preparada para múltiplos formatos
* extensibilidade priorizada sobre complexidade precoce
* `src/` isolado para evitar imports acidentais
* exceções de domínio separadas da camada HTTP
* classes de conversão seguindo padrão Strategy
* ferramentas de lint usadas como apoio à qualidade, não como dogma


