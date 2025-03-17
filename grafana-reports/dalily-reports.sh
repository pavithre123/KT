#!/bin/bash

# export GRAFANA=false
# export KIBANA=false

if [[ "$GRAFANA" == "true" ]]; then
    echo "Grafana reports enabled!!!"
    cd grafana
    sh dalily-reports-grafana.sh
elif [[ "$GRAFANA" == "false" ]]; then
    echo "Grafana reports not enabled!!!"
else
    echo "set GRAFANA environment variable!!!"
    exit -1
fi

if [[ "$KIBANA" == "true" ]]; then
    echo "Kibana reports enabled!!!"
    cd kibana
    sh dalily-reports-kibana.sh
elif [[ "$KIBANA" == "false" ]]; then
    echo "Kibana reports not enabled!!!"
else
    echo "set KIBANA environment variable!!!"
    exit -1
fi

