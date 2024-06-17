# Use a imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY . .

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
