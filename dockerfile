# Dockerfile für die Basis des Telegram Bot

# Verwende ein Python-Basisimage
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis innerhalb des Containers
WORKDIR /app

# Kopiere die Anwendungsabhängigkeiten
COPY requirements.txt .

# Installiere die Anwendungsabhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Anwendungscode in das Arbeitsverzeichnis im Container
COPY . .

# Starte den Telegram Bot
CMD ["python", "telegram_bot.py"]
