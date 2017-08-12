# Preparing your Mac
## Add Test URLs 
*NEEDS:* wagtail, cherrypy and nginx are already configured

- edit hosts (as superuser)
`sudo nano /private/etc/hosts`
- add
`{{ip-address}} {{test-domain-name-1}} {{test-domain-2}}`
 e.g. myserver.test
- save and exit nano
- run `server_ 
- test in safari with `http://{{test-domain-name-1}}` 



## Reset SSH-Keys

If you had an earlyer instance on the same IP-address you might no remove the information from your Mac with the following steps

-delete old entry to server in file /Users/{{username}}.ssh/keygen
