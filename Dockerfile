FROM python:3.10.4-slim-bullseye
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME=/code
# RUN mkdir $HOME
# RUN mkdir $HOME/staticfiles
WORKDIR $HOME
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .