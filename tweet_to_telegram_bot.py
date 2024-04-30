# Dockerfile for the base of the Telegram Bot

# Use a Python base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy the application dependencies
COPY requirements.txt .

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory in the container
COPY . .

# Set the environment variable for the Telegram Bot Token
ENV TOKEN $TELEGRAM_BOT_TOKEN

# Start the Telegram Bot
CMD ["python", "tweet_to_telegram_bot.py"]
