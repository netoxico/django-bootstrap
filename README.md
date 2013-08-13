## Django bootstrap project template
### Includes
* twitter bootstrap 3
* django-annoying
* django-compressor
* 

### How to use
Create virtual environment, change project_name with your projects name :D
```sh
mkvirtualenv project_name
```

Run django startproject with the --template option
```
django-admin.py startproject --template=https://github.com/netoxico/django-bootstrap/archive/master.zip project_name
```

Install requirements
```sh
pip install -r requirements/development.txt
```

Set DJANGO_SETTINGS_MODULE environment
```sh
sudo sh -c 'echo "export DJANGO_SETTINGS_MODULE=development" >> /etc/profile.d/environment.sh' && source /etc/profile.d/environment.sh
```
Done.
