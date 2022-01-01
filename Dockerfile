FROM python:3.8.12

## PIP Requirements
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt --no-cache-dir

ENV PYTHONPATH=/app
COPY app /app
COPY frontend/home.html /app
WORKDIR /app

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "main:app"]