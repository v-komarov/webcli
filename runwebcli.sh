#!/bin/bash

/usr/bin/docker run -d -p 5000:5000 \
--name webcli \
--link freeradiusdb:mysql \
-e MYSQL_HOST=mysql \
-e RADTEST_HOST=10.6.2.251 \
webcli:seventh
