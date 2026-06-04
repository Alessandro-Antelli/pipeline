FROM python:3.11-alpine

WORKDIR /app

# Copia prima il file dei requisiti
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del codice (cartella app inclusa)
COPY . .

# Comando per eseguire l'analisi
CMD ["python", "app/analyzer.py"]