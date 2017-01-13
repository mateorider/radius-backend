#! /bin/bash
python /radius/manage.py migrate --noinput
python /radius/manage.py runserver 0.0.0.0:8000
