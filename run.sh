#!/bin/bash

# This script is used to build all necessary python components
# and runt django website.
lay_egs() {
  # The directory path is sent as the first argument
  cd $1
  pwd
  python setup.py install
  cd ..
}

run_server() {
  # The Django website path is sent as the first argument
  cd $1
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
}

# clean
source clean.sh

# build components
lay_egs D3Core
lay_egs parser_json
#lay_egs parser_xml
#lay_egs visualization_complex
#lay_egs visualization_simple
run_server django_project
