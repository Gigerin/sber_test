FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /sber_test

RUN apt-get update && apt-get install -y curl build-essential && poetry install --no-root --no-dev

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY . /sber_test

EXPOSE 5000

CMD ["poetry", "run", "python", "app.py"]
