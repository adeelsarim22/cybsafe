# Cybsafe

### Pre-requisites:
python-version: 3.10


### Create virtualenv and activate it
 
```bash
 python -m virtualenv venv

 ```

```bash
source venv/bin/activate
 ```

### Install Requirements
 
```bash
 pip install -r requirements.txt
 ```

### To execute migrations:

```bash
python manage.py migrate
```

### To execute the project:

```bash 
python manage.py runserver
```

### To execute the tests:

```bash 
pytest
```

### Swagger Schema for API Documentation:

 Go to url `api/schema/swagger-ui/` and execute the API
