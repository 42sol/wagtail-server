# wagtail-server
Creating a Server For Wagtail Project (Documentation and Scripts) using linode and ubuntu-linux 

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

#### Setup IP and Hostnameh
```bash
echo “{{hostname}}” > /etc/hostname
hostname -F /etc/hostname
ls /etc/default
nano /etc/hosts
```
- Insert your IP-address and name and URL(?) 
- and save
- test hostname
```bash
hostname
```

- Install Python 3
```bash
```



- add {{ipp-address}} 172.104.128.206

### Setup Webserver
### Setup WSGI-Server
### Setup Django 
### Setup Wagtail

----
[login linode]:https://manager.linode.com
[marco.org]: https://marco.org
[wagtail]: https://wagtail.io
