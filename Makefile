
setup:
	wget -nc https://releases.hashicorp.com/consul/1.11.4/consul_1.11.4_linux_amd64.zip && \
	mkdir -p ./dictionary_service/libs && \
	mkdir -p ./expression_service/libs && \
	cp consul_1.11.4_linux_amd64.zip ./dictionary_service/libs && \
	cp consul_1.11.4_linux_amd64.zip ./expression_service/libs

docker-build: setup
	docker build ./dictionary_service/ --tag dictionary_service && \
	docker build ./expression_service/ --tag expression_service

services-up: docker-build
	docker-compose up --build
