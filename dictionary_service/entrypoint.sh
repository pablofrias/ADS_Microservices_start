#!/bin/bash
consul agent -node=client-dictionary$(hostname -i) -config-dir=/etc/consul.d -join=consul --data-dir /path/to/datadir &
python server.py