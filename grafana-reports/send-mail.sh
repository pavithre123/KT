#!/bin/bash

# Variables
FROM="pavithra.rathnayake@axiatadigitallabs.com"
TO="hasith.senevirathne@axiatadigitallabs.com"
SUBJECT="Here is an image"
BODY="Please find the attached image."
IMAGE_PATH="/grafana-reports/scripts/dashboard_area.png"
IMAGE_NAME="dashboard_area.png"

# Encode the image in base64
MIME_TYPE=$(file --mime-type -b "$IMAGE_PATH")
ENCODED_IMAGE=$(base64 "$IMAGE_PATH")

# Create the email content with attachment
(
echo "From: $FROM"
echo "To: $TO"
echo "Subject: $SUBJECT"
echo "MIME-Version: 1.0"
echo "Content-Type: multipart/mixed; boundary=\"BOUNDARY\""
echo
echo "--BOUNDARY"
echo "Content-Type: text/plain; charset=UTF-8"
echo "Content-Transfer-Encoding: 7bit"
echo
echo "$BODY"
echo
echo "--BOUNDARY"
echo "Content-Type: $MIME_TYPE; name=\"$IMAGE_NAME\""
echo "Content-Disposition: attachment; filename=\"$IMAGE_NAME\""
echo "Content-Transfer-Encoding: base64"
echo
echo "$ENCODED_IMAGE"
echo
echo "--BOUNDARY--"
) | sendmail -t