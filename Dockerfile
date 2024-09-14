FROM python:3.12-slim

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

COPY wsgi.py .
EXPOSE 5000

CMD ["waitress-serve", "--threads=4", "--host=0.0.0.0", "--port=5000", "wsgi:app"]