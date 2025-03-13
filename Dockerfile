# Python-Image
FROM python:3.13.2-slim

# Arbeitsverzeichnis im Container setzen
WORKDIR /app

# Kopiere alle Dateien in das Arbeitsverzeichnis des Containers
COPY src /app

# Das Python-Skript ausführen
CMD ["python", "main.py"]
