FROM python:3.12

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./app /app

# On compile Flask uniquement depuis les sources
RUN pip install --no-cache-dir --no-binary flask flask==2.2.5

# On installe le reste normalement
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]


