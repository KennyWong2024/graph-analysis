FROM python:3.11-slim

WORKDIR /app

ENV PIP_NO_CACHE_DIR=1

COPY routing-service/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY routing-service/app    ./app
COPY common                 ./common
COPY graph_normalizer       ./graph_normalizer

EXPOSE 8002

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
