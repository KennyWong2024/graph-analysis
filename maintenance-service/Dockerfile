FROM python:3.11-slim

WORKDIR /app

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MAINT_TZ=America/Costa_Rica

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY app  ./app
COPY data ./data

EXPOSE 8003

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8003"]
