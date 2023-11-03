FROM python:3.11.2

WORKDIR /home/Django_docker

RUN groupadd --gid 1000 django && useradd --uid 1000 --gid django --shell /bin/bash --create-home django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY docker_web/requirements.txt /home/Django_docker/requirements.txt

RUN pip install -r requirements.txt

COPY ./docker_web /home/Django_docker/

RUN chown -R django:django /home/Django_docker/

RUN ["chmod", "+x", "/home/Django_docker/entrypoint.sh"]
