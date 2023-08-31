FROM python:3.11.5-slim


ENV APP_HOME /app

WORKDIR $APP_HOME

COPY Book/ .

ENTRYPOINT ["python", "bot.py"]