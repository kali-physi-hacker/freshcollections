#!/bin/bash

mode=$1

if [ $# -lt 1 ]
then
  echo "No argument passed"
  echo "Available args"
  echo "---------------"
  echo "-d or --development"
  echo "-p or --production"
  echo
  echo "Example Usages:"
  echo "./runserver --development    -   That runs the server in development mode"
  echo "./runserver -p               -   That runs the server in production mode"

  exit
fi

if [ $mode == "-d" ] || [ $mode == "--development" ]
then
    export DJANGO_SETTINGS_MODULE=estore.settings.dev
elif [ $mode =="-p" ] || [ $mode == "--production" ]
then
    export DJANGO_SETTINGS_MODULE=estore.settings.prod
fi

python manage.py runserver
