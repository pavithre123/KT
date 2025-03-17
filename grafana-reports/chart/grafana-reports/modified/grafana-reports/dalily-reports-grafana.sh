#!/bin/bash

echo "Grafana dailly reports generation started..."
python3 ss_grafana.py
python3 inline-mail.py
