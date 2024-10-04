#!/bin/bash

pip install ssl
CREDENTIALS_FILE = 'credentials.txt'

read -p "Enter email address: " email
read -sp "Enter email password: " password

echo "$email" > "$CREDENTIALS_FILE"
echo "$password" >> "$CREDENTIALS_FILE"

echo "Setup complete and credentials saved!"