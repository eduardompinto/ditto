FROM python:3.8.12-bullseye

## PIP Requirements
RUN pip install --upgrade pip pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt --no-cache-dir

COPY app /app
WORKDIR /app
ENV PYTHONPATH=/app

CMD uvicorn main:app --host 0.0.0.0 --port $PORT