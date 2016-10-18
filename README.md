# Buddy

## Developer enviroment

Create virtualenv and activate

```bash
virtualenv .env
source .env/bin/activate
```

Install requirements

```bash
pip install -r requirements/dev.txt
```

Create your own settings from example

```bash
cp local_settings.py.dist local_settings.py
```

Create developer database

```bash
python manage.py migrate
```

Run developer server

```bash
python manage.py runserver
```
