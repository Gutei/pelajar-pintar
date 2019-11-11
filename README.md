**INSTALATION**

Create pyhton virtual environment
```
$ python3.6 -m venv venv
```

Source to virtual environment
```
$ source venv/bin/activate
```

Install all requirements using pip
```
$ pip install -r requirements.txt
```

Enter the project directory _**dash**_:
```
$ cd dash
```

Export to environment variable the application settings
```
$ export DJANGO_SETTINGS_MODULE=dash.your_settings
```

Migrate all migrations (change database connection in the settings file):
```
$ ./manage.py migrate
```

Create superuser
```
$ ./manage.py createsuperuser
```

Don't forget to collect all static files
```
$ ./manage.py collectstatic
```

Run it!
```
$ ./manage.py runserver
```