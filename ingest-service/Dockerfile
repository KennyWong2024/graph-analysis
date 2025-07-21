FROM python:3.11-slim
WORKDIR /app
ENV PIP_NO_CACHE_DIR=1


COPY ingest-service/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY ingest-service/app    ./app
COPY common                ./common

EXPOSE 8001
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
