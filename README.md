# wagtail-server
Creating a Server For Wagtail Project (Documentation and Scripts) using linode and ubuntu-linux 

WARNING: still under construction !!
TODO: find a solution to serve static data (/media) with nginx from multiple folders
TODO: find a solution to serve different wsgi apps with cherrypy (server_wagtail.py imports one application from specific module) -> run it more than once ? load all applications?
TODO: change bash-scripts to python (because I suck in bash programming)

## Setup
- Server runs on a [linode] server
- Server is a Ubuntu v16.06-LTS
- App with Wagtail  vLast
- Python 3 (vLast)
  - pip
  - django

## Links
### Basic
- Login to Linode with [login linode]
- Wagtail Documention on [wagtail]

### Further Reading
- Always helpful [marco.org]

## Setup
### Preparing your Mac
#### Reset SSH-Keys
If you had an earlyer instance on the same IP-address you might no remove the information from your Mac with the following steps
- delete old entry to server in file \Users\{{username}}\.ssh\keygen


### Preparing the Server
- Create a new or a valid container in Linode Manager
- Login via SSH as root
- Update installer repositories 
```bash
apt-get update && apt-get upgrade
```
- Watch and evaluate the progress

#### Setup IP and Hostnameh
```bash
echo “{{hostname}}” > /etc/hostname
hostname -F /etc/hostname
ls /etc/default
nano /etc/hosts
```
- Insert your IP-address and name and URL(?) 
- and save
- test hostname and URL(?)
```bash
hostname
hostname -f
```
- check your correct name for the server

#### Timezone
- Use timezone configuration
```bash
dpkg-reconfigure tzdata
```
- Select your desired configuration

#### Basic Tools
- Install PIP 3
```bash
sudo apt-get install python3-pip
```

- Check  Python 3 and PIP Versions
```bash
python3 -V
pip3 -V
```

### Wagtail Application
- install cherrypy
```bash
sudo pip3 install cherrypy
```
- install Wagtail (last version)
```bash
sudo pip3 install wagtail
```
- write cherrypy server 
- create file with `server_wagtail.py`
- use content of `server_wagtail.py` from correspoinding setup folder
- save file and leave nano

- setup a new wagtail project with `scripts\wagtail\0_setup-project.sh`
- add '{{ip-address}}' and 'localhost' to ALLOWED_HOSTS in ```settings\base.py``` of all projects
- run cherrypy from folder as manage.py of your project
```bash
python3 server_{{project-name}}.py
```
- go to admin page 
- login 
- check functions


TODO: Extend the HomePage model http://docs.wagtail.io/en/v1.11.1/getting_started/tutorial.html#extend-the-homepage-model


### Setup Webserver
### Setup WSGI-Server
### Setup Django 
### Setup Wagtail

----
[login linode]:https://manager.linode.com
[marco.org]: https://marco.org
[wagtail]: https://wagtail.io

### TODO-> master with virtualenv
sudo pip install virtualenv
sudo virtualenv {{project-name}}_virtualenv # a virtual python environment 
source {{project-name}}_virtualenv/bin/activate # will activate 

