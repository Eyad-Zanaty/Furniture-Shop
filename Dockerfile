FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    libmariadb-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
