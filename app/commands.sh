#!/bin/bash

cd /home/cosmin/Programare/PROJECTS/Licenta/dcae-website-master-5cb3767e5e71f234f8dd07b80a6f2b72b6a1c12c/app

export DJANGO_SETTINGS_MODULE=settings
./manage.py ${*}