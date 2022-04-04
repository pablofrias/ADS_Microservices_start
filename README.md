# UTN-FRC Sentiment Analysis for Microservices class

Sentiment Dictionary example for Arquitectura de Software - UTN-FRC 2020

## Table of Contents

## Prerequisites

### Dependencies

- Python 3.8
  - How to install latest stable release [here](https://tecadmin.net/install-python-3-8-ubuntu/)

## Getting Started

Run Consul server:

  - sudo docker run -d --ip 172.17.0.2 -p 8500:8500 -p 8600:8600/udp --name=badger  consul agent -server -ui -node=server-1 -bootstrap-expect=1 -client=0.0.0.0

  Please note that the static ip 172.17.0.2 might not work on your environment. You can change entrypoint.sh on both services to set the consul IP address manually.

Verify Consul server is running at http://172.17.0.2:8500/

Create docker images for dictionary service:
  - cd dictionary_service/
  - sudo docker build -t ads/dictionary .

Run Dictionary service:
  - sudo docker run -d -t ads/dictionary

Check Dictionary service:
  - curl http://172.17.0.3:5000/dictionary/api/v1.0/words/deny

Create docker images for expression service:
  - cd expression_service/
  - sudo docker build -t ads/expression .

Run Expression Service:
  - sudo docker run -d -t ads/expression

Check Expression service:
  - curl http://172.17.0.5:5000/expression/api/v1.0/sentiment/great%20job

Verify Consul is showing dictionary & expression clients in the UI

### Style Guide

- [PEP8](https://www.python.org/dev/peps/pep-0008/)

## Authors

- **FRÍAS, Pablo** - _pablosfrias@gmail.com_
