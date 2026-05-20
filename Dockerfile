FROM --platform=linux/amd64 python:3.13-slim

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get clean && rm -rf /var/lib/apt/lists/* && apt-get update && apt-get upgrade -y && \
    # Insert additional package installations here if needed \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /service

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .
COPY app/templates templates
COPY app/static static

EXPOSE 5000

CMD ["waitress-serve", "--threads=4", "--host=0.0.0.0", "--port=5000", "app:app"]