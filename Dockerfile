# Imagem base enxuta e estável

FROM python:3.14.2-slim

# Evita arquivos .pyc e ativa logs imediatos

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho

WORKDIR /app

# Instala dependências de sistema mínimas

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivos de dependências primeiro (cache eficiente)

COPY pyproject.toml README.md ./

# Instala dependências do projeto

RUN pip install --upgrade pip && pip install .

# Copia o restante do código

COPY src ./src
COPY main.py ./

# Porta padrão do FastAPI

EXPOSE 8000

# Comando de inicialização

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
