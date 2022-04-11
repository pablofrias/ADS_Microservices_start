#!/bin/bash
consul agent -join=172.17.0.2 -node=client-dictionary$($echo $(hostname -i) | tr . -) -config-dir=/etc/consul.d --data-dir /path/to/datadir &
python server.py