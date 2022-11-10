FROM python:3.8-slim as base

# add requirements
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN  pip install -r requirements.txt

FROM base as app

WORKDIR /app

ENTRYPOINT ["python", "manage.py"]

COPY ./ /app/
