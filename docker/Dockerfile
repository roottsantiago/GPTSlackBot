FROM python:3.8.13

ARG APP=/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR ${APP}

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . ${APP}

ENTRYPOINT ["python"]
CMD ["app.py"]
