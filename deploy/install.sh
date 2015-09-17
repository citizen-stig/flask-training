#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y postgresql python-dev python-pip libpq-dev libssl-dev libffi-dev libxml2-dev libxslt1-dev

sudo pip install -r requirements.txt

sudo -u postgres bash -c "psql -c \"CREATE USER flask WITH PASSWORD 'flask';\""
sudo -u postgres bash -c "psql -c \"ALTER USER flask CREATEDB;\""
sudo -u postgres bash -c "psql -c \"CREATE DATABASE flask ENCODING 'UTF8';\""
sudo -u postgres bash -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE flask to flask;\""
