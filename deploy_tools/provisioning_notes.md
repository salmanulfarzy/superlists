Provisioning a new site
========================

## Required packages:
- nginx
- Python 3.6
- Git
- pip
- virtualenv

e.g, on Ubuntu

```sh
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get install nginx git python3.6 python3.6-venv
```

## nginx host configuration
- see [nginx.template.conf](https://github.com/sfarzy/superlists/blob/master/deploy_tools/nginx.template.conf)
- replace SITENAME with staging site name

## System service
- see [gunicorn-systemd-template.service[(https://github.com/sfarzy/superlists/blob/master/deploy_tools/gunicorn-systemd.template.service)
- replace SITENAME with staging site name

## Folder structure
Assume we have a user accuont at /home/username
```
/home/username
|__ sites
    |__ SITENAME 
        |__ database
        |__ source
        |__ static
        |__ virtualenv
```
