FROM python:3.10.0a7-buster

RUN mkdir -p /usr/src/app && \
    apt update && \
    apt install net-tools

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    mv wait-for-it.sh /usr/sbin

COPY ./libs/consul_1.7.2_linux_amd64.zip .

RUN unzip consul_1.7.2_linux_amd64.zip && \
    cp consul /usr/sbin && \
    mkdir -p /etc/consul.d

COPY entrypoint.sh /usr/local/sbin/

COPY consul_service.json /etc/consul.d/dictionary.json

WORKDIR /usr/src/app

ADD . /usr/src/app

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "./entrypoint.sh" ]