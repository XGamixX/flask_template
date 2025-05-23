FROM python:3.13-slim

WORKDIR /service

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .
COPY app/templates templates
COPY app/static static

EXPOSE 5000

CMD ["waitress-serve", "--threads=4", "--host=0.0.0.0", "--port=5000", "app:app"]