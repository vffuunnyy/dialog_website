FROM python:3.12 as compile-image
LABEL authors="vffuunnyy"

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /
COPY . .

CMD ["uvicorn", "--host=0.0.0.0", "--port=40203", "src.main:app"]