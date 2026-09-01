# File Converter

Projeto backend para **conversão de arquivos**, desenvolvido como um **sistema extensível de file-converter**, com foco em **arquitetura limpa**, **qualidade de código** e **boas práticas profissionais**.

Este projeto foi pensado como item de **portfólio**, demonstrando organização de código, testes, lint, automação, portabilidade e **capacidade de evolução para múltiplos conversores**.

---

## 🧠 Visão do Sistema

O **File Converter** é o sistema principal.

Atualmente, ele possui **três conversores implementados**:

* **CSV → XLSX**
* **JSON → CSV**
* **XML → XLSX**

A arquitetura foi desenhada para permitir a adição de novos conversores (ex: JSON → CSV, XML → XLSX) **sem alterar o core do sistema**.

---

## 🧱 Arquitetura

O projeto segue uma separação clara de responsabilidades:

* **API**: camada HTTP (FastAPI)
* **Services**: orquestração e regras de aplicação
* **Converters**: lógica pura de conversão
* **Domain**: contratos e abstrações

```
src/
├── csv_to_xlsx/            # Módulo CSV → XLSX
│   ├── api/                # Camada HTTP (FastAPI)
│   ├── services/           # Orquestração do sistema
│   ├── converters/         # Conversores de arquivos
│   │   └── csv_to_xlsx.py  # Implementação CSV → XLSX
│   └── domain/             # Abstrações e contratos
└── json_to_csv/            # Módulo JSON → CSV
    ├── api/                # Camada HTTP (FastAPI)
    ├── services/           # Orquestração do sistema
    ├── converters/         # Conversores de arquivos
    │   └── json_to_csv.py  # Implementação JSON → CSV
    └── domain/             # Abstrações e contratos
└── xml_to_xlsx/            # Módulo XML → XLSX
    ├── api/                # Camada HTTP (FastAPI)
    ├── services/           # Orquestração do sistema
    ├── converters/         # Conversores de arquivos
    │   └── xml_to_xlsx.py  # Implementação XML → XLSX
    └── domain/             # Abstrações e contratos
    └── domain/             # Abstrações e contratos

tests/                      # Testes automatizados
main.py                     # Entry point da aplicação
```

---

## 🚀 Tecnologias

* Python 3.14+
* FastAPI
* Pandas
* OpenPyXL
* Pytest
* Ruff / Black / Pylint
* Docker
* GitHub Actions (CI)

---

## ▶️ Executando localmente

### 1️⃣ Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2️⃣ Instalar dependências

```bash
pip install -e .[dev]
```

### 3️⃣ Subir a aplicação

```bash
uvicorn main:app --reload
```

Acesse:

```
http://localhost:8000/docs
```

---

## 🐳 Executando com Docker

```bash
docker build -t file-converter .
docker run -p 8000:8000 file-converter
```

---

## 🧪 Testes

```bash
pytest
```

---

## 🧹 Qualidade de código

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

## 🎯 Decisões arquiteturais

* **File Converter** tratado como sistema central

* cada conversão implementa um contrato comum (`Converter`)

* conversores isolados da camada HTTP

* arquitetura preparada para múltiplos formatos

* extensibilidade priorizada sobre complexidade precoce

* `src/` isolado para evitar imports acidentais

* exceções de domínio separadas da camada HTTP

* classes de conversão seguindo padrão Strategy

* ferramentas de lint usadas como apoio à qualidade, não como dogma

---

## ✨ Próximos passos

* adicionar novos conversores (ex: XLSX → CSV)
* endpoint de download direto do arquivo
* métricas e observabilidade
* autenticação
