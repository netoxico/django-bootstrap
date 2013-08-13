## Django bootstrap project template
### Includes
* Twitter bootstrap 3
* django-annoying
* django-compressor
* django-debug-toolbar
* django-extensions

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

Set 'DJANGO_SETTINGS_MODULE' environment. Make shure to change project_name
* 'project_name.settings.development'
* 'project_name.settingsproduction',
* 'project_name.settingsstaging'

For development environment:
```sh
sudo sh -c 'echo "export DJANGO_SETTINGS_MODULE=project_name.settings.development" \
>> /etc/profile.d/environment.sh' && source /etc/profile.d/environment.sh
```
Done.
