#!/usr/bin/env bash

../../../wait
# Add migrations
python manage.py migrate

# Add a door for an external commands
exec python manage.py $@
