## Scripts For Wagtail
I find the following scripts helpfull for my personal usage

- `1_startapp.sh APP_NAME`: use manage.py to create a new app
- `2_update.sh`: use manage.py to call makemigrations and migrate in one go
- `3_run.sh`[^run.sh]: use local cherrypy-script to run the wsgi-server 
- `9_backup.sh NOTE`: use `zip` to make a quick backup from the local directory

[^run.sh]: used until the wsgi-server (cherrypy) runs from services
