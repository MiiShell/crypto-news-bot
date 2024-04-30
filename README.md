## YourCryptoInsightBot








### Docker

Um das Dockerfile auszuführen, führe die folgenden Schritte aus:

Stelle sicher, dass Docker auf deinem System installiert ist.
Navigiere im Terminal zum Verzeichnis, das dein Dockerfile enthält.
Baue das Docker-Image mit dem folgenden Befehl:

docker build -t mein_telegram_bot .


Hierbei wird ein Docker-Image mit dem Namen mein_telegram_bot erstellt. Du kannst den Namen entsprechend anpassen.
Führe den erstellten Container mit dem folgenden Befehl aus:
arduino

docker run --rm -it mein_telegram_bot

Dadurch wird der Container ausgeführt und dein Telegram Bot wird gestartet.
Wenn du spezifische Konfigurationen oder Umgebungsvariablen benötigst, kannst du den Befehl docker run entsprechend anpassen.