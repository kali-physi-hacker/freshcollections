#!/bin/bash

mode=$1

if [ $# -lt 1 ]
then
  echo "No argument passed"
  echo "Available args"
  echo "---------------"
  echo "createsuperuser"
  echo "makemigrations"
  echo "migrate"
  echo "test"
  echo
  echo "Example Usages:"
  echo "./runserver createsuperuser"

  exit
fi

if [ "$mode" == "-d" ] || [ "$mode" == "--development" ]
then
    export DJANGO_SETTINGS_MODULE=estore.settings.dev
elif [ "$mode" == "-p" ] || [ "$mode" == "--production" ]
then
    export DJANGO_SETTINGS_MODULE=estore.settings.prod
fi
#echo $2
python manage.py "$2"
