Provisioning a new site
=====================
## Requirements
* nginx
* Python 3.6
* virtualenv
* Git

for example in Ubuntu:

    sudo apt-get install nginx git python36 python3.6-venv
    
## Config virtual host Nginx

* nginx.template.conf
* replace SITENAME, for example, with staging.my-domain.com

## Systemd

* gunicorn-systemd.template.service
* replace SITENAME, for example, with staging.my-domain.com
