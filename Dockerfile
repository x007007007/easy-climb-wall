FROM python3.10 as base
RUN apt-get update \
    && pip install -U pdm pip wheel setuptools
FOROM base as builder

WORKDIR /opt/builder
COPY ./pyproject.toml ./
COPY ./pdm.lock ./
RUN pdm install
