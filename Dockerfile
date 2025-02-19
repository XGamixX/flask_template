FROM python:3.13-slim

WORKDIR /service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates templates
COPY static static

EXPOSE 5000

CMD ["waitress-serve", "--threads=4", "--host=0.0.0.0", "--port=5000", "app:app"]