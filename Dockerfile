FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./server_py/ .

RUN pip install --no-cache-dir -r requirements.txt