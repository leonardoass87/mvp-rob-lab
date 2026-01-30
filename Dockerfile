FROM python:3.9-slim

WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos (incluindo o app.py)
COPY . .

CMD ["python", "app.py"]