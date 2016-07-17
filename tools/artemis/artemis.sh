#!/bin/bash
broker_addr=${BROKER_ADDR}
broker_port=${BROKER_PORT}
client_ident=${IDENT}
client_secret=${SECRET}

sed -i "s/<broker_addr>/$broker_addr/g" /opt/thug/src/Logging/logging.conf
sed -i "s/<broker_port>/$broker_port/g" /opt/thug/src/Logging/logging.conf
sed -i "s/<ident>/$client_ident/g" /opt/thug/src/Logging/logging.conf
sed -i "s/<secret>/$client_secret/g" /opt/thug/src/Logging/logging.conf

sed -i "s/<broker_addr>/$broker_addr/g" /opt/thug/tools/artemis/linkreceiver.py
sed -i "s/<broker_port>/$broker_port/g" /opt/thug/tools/artemis/linkreceiver.py
sed -i "s/<ident>/$client_ident/g" /opt/thug/tools/artemis/linkreceiver.py
sed -i "s/<secret>/$client_secret/g" /opt/thug/tools/artemis/linkreceiver.py

python /opt/thug/tools/artemis/linkreceiver.py
