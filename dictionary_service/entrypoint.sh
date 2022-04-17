#!/bin/bash
consul agent -join=consul -node=client-dictionary$(echo $(hostname -i) | tr . -) -config-dir=/etc/consul.d --data-dir /path/to/datadir &
python server.py