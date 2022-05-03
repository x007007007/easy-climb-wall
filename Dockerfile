FROM python:3.10 as base
RUN apt-get update \
    && apt-get install -y shadowsocks-libev \
    && pip install -U pdm pip wheel setuptools \
    && wget https://github.com/shadowsocks/v2ray-plugin/releases/download/v1.3.1/v2ray-plugin-linux-amd64-v1.3.1.tar.gz \
    && tar -xzvf v2ray-plugin-linux-*-v1.3.1.tar.gz -C /bin/ \
    && ln -s /bin/v2ray-plugin_linux_amd64 /bin/v2ray-plugin
FROM base as builder

WORKDIR /opt/builder
COPY ./pyproject.toml ./
COPY ./pdm.lock ./
RUN pdm install

COPY ./ ./
RUN pdm install && pdm build

FROM base
WORKDIR /opt/easyclimbwall
COPY --from=build dist/ ./
RUN pip install easy_climb_wall-0.1.0-py3-none-any.whl \
    && python -m x007007007.easyclimbwall collectstatic  --no-input
ENV DATA_FOLDER=/data \
    SS_SERVER_CMD=ss-server \
    SS_V2RAY_PLUGIN_PATH=/bin/v2ray-plugin_linux_amd64 \
    DOCKER_SERVICE_NAME=climb-wall-config \
    SECRET_KEY=

CMD ['gunicron', 'x007007007.easyclimbwall.wsgi:application', '-k', 'gevent']

