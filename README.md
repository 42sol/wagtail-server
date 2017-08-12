# wagtail-server
Creating a Server For Wagtail Project (Documentation and Scripts) using linode and ubuntu-linux 

TODO: still under construction !!

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
- create file with ```nano server_{{project-name}}.py#```
- insert
```python
# Import your application as:
# from wsgi import application
# Example:

from test_setup.wsgi import application

# Import CherryPy
import cherrypy

if __name__ == '__main__':

    # Mount the application
    cherrypy.tree.graft(application, "/")

    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    # Instantiate a new server object
    server = cherrypy._cpserver.Server()

    # Configure the server object
    server.socket_host = "0.0.0.0"
    server.socket_port = 8001
    server.thread_pool = 30

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

    # Subscribe this server
    server.subscribe()

    # Example for a 2nd server (same steps as above):
    # Remember to use a different port

    # this file comes from anoter tutorial 
    # Subscribe this server
    server.subscribe()

    # Example for a 2nd server (same steps as above):
    # Remember to use a different port

    # server2             = cherrypy._cpserver.Server()

    # server2.socket_host = "0.0.0.0"
    # server2.socket_port = 8081
    # server2.thread_pool = 30
    # server2.subscribe()

    # Start the server engine (Option 1 *and* 2)

    cherrypy.engine.start()
    cherrypy.engine.block()
```
- save file

- setup a new wagtail project
```bash
wagtail start {{project-name}} # setup the project
cd {{project-name}}            # setup the database
python3 manage.py migrate
python3 manage.py createsuperuser # create an administrator account
python3 wagtail_server.py
```
- add '{{ip-address}}' and 'localhost' to ALLOWED_HOSTS in ```settings\base.py```
- run cherrypy from folder as manage.py of your project
```bash
python3 server_{{project-name}}.py
```
- go to admin page 
- login 
- check functions





- add {{ip-address}} 172.104.128.206

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

