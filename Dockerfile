# Docker-команда FROM указывает базовый образ контейнера
# Наш базовый образ - это Linux с предустановленным python-3.10
FROM python:3.10

# Установим переменную окружения
ENV APP_HOME /program

# Установим рабочую директорию внутри контейнера
WORKDIR $APP_HOME

COPY poetry.lock $APP_HOME/poetry.lock
COPY pyproject.toml $APP_HOME/pyproject.toml

# Установим зависимости внутри контейнера
RUN pip install poetry
RUN poetry virtualenvs.create false && install --only main

# Скопируем остальные файлы в рабочую директорию контейнера
COPY . .


# Обозначим порт где работает приложение внутри контейнера
EXPOSE 5000

# Запустим наше приложение внутри контейнера
CMD ["python3", "money_manager/run.py"]