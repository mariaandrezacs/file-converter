# File Converter

Projeto backend para **conversão de arquivos**, desenvolvido como um **sistema extensível de file-converter**, com foco em **arquitetura limpa**, **qualidade de código** e **boas práticas profissionais**.

Este projeto foi pensado como item de **portfólio**, demonstrando organização de código, testes, lint, automação, portabilidade e **capacidade de evolução para múltiplos conversores**.

---

## Visão do Sistema

O **File Converter** é o sistema principal.

Atualmente, ele possui os seguintes conversores implementados:

* **CSV → JSON**
* **CSV → XLSX**
* **CSV → XML**
* **JSON → CSV**
* **JSON → XLSX**
* **JSON → XML**
* **TXT → CSV**
* **XLSX → CSV**
* **XLSX → JSON**
* **XLSX → XML**
* **XML → CSV**
* **XML → JSON**
* **XML → XLSX**

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
├── core/                   # Contratos e rotas compartilhadas
│   ├── converter.py
│   └── routes.py
├── csv_to_json/            # Módulo CSV → JSON
├── csv_to_xlsx/            # Módulo CSV → XLSX
├── csv_to_xml/             # Módulo CSV → XML
├── json_to_csv/            # Módulo JSON → CSV
├── json_to_xlsx/           # Módulo JSON → XLSX
├── json_to_xml/            # Módulo JSON → XML
├── txt_to_csv/             # Módulo TXT → CSV
├── xlsx_to_csv/            # Módulo XLSX → CSV
├── xlsx_to_json/           # Módulo XLSX → JSON
├── xlsx_to_xml/            # Módulo XLSX → XML
├── xml_to_csv/             # Módulo XML → CSV
├── xml_to_json/            # Módulo XML → JSON
└── xml_to_xlsx/            # Módulo XML → XLSX

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

---

## Próximos passos

* adicionar validação de tipos MIME e extensão
* métricas e observabilidade
* autenticação
* expansão para PDF, imagens, YAML, Markdown e Base64
