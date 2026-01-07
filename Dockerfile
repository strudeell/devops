FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY data_base.py .
COPY model_1.pkl .
COPY data.csv .
COPY website_data.db .


EXPOSE 7860

CMD ["python", "app.py"]
