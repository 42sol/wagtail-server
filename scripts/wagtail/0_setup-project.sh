#!/bin/bash

#if [-z "$1"] 
#then
#  echo "-[error1] invalid parameter-1=$1 - is empty"
#  return 1
#fi
#
#if [-d "$1"] 
#then
#  echo "-[error2] invalid parameter-1=$1 - already exists"
#  return 2
#fi

echo "-[1] setup project (parameter-1=$1)"
wagtail start $1 # setup the project
cd $1            # setup the database
echo "-[2] prepare for running (migrate)"
python3 manage.py migrate
echo "-[3] create a superuser account"
echo "     hit CTRL-C if all is fine"
echo ""
python3 manage.py createsuperuser # create an administrator account
echo "-[4] run the development server - only to see if all is fine"
python3 manage.py runserver
echo "-[5] copy script to project folder"
cp ../*.sh .
rm -f 0_*.sh # this script is not needed here
echo "-[6] back to apps folder"
cd ..
