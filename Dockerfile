FROM python:alpine3.6

RUN apk update && \
    apk add curl && \
    apk add make && \
    rm -rf /var/cache/apk/* && \
    mkdir /app

WORKDIR /app

ENTRYPOINT ["make", "run"]
