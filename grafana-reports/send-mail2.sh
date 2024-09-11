#!/bin/bash

today=$(date | awk '{print $2, $3, $7}')

sender="nagios@robi.com"
recipient="pavithra.rathnayake@axiatadigitallabs.com"
subject="ROBI IGW-STAGING DAILY SERVER HEALTH CHECK REPORT - $today"
# html_file_path="$HOME/monitoring/report/prod/server_report.html"  

log_file="$HOME/monitoring/summery-prod.log"

# if ! [ -f "$html_file_path" ]; then
#   echo "Error: HTML file '$html_file_path' not found."
#   exit 1
# fi


(
  echo "Subject: $subject"
  echo "From: $sender"
  echo "To: $recipient"
  echo "Content-Type: text/html"
  echo
#   cat $html_file_path
) | sendmail -t -f "$sender"


