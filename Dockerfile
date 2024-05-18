FROM python:3.9

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install gunicorn==20.1.0

COPY req.pip .

RUN pip install --no-cache-dir -r req.pip

COPY . .

RUN chmod +x /usr/src/app/web-entrypoint.sh
