# 29415_52665_52668_51413
AEH Projekt na przedmioty: Aplikacyjny projekt zespołowy i Projektowanie wielowarstwowych aplikacji biznesowych.
SimpCRM App

## Pierwsze uruchamianie aplikacji:

### 1. Terminal:
```
git clone https://github.com/McRas/29415_52665_52668.git
```
Wejdź w folder /29415_52665_52668
```
python -m venv wirtual
```
```
pip install -r requirements.txt
```

### 2. Zaktualizuj dane dotyczące swojej MYSQL database w pliku settings.py i mydb.py
(domyślnie 	user = 'root', hasło = '1234')

### 3. Terminal:
```
python manage.py runserver
```
Opcjonalnie:
```
python manage.py createsuperuser
```
### 4. Uruchom: http://127.0.0.1:8000/

## Kolejne uruchamianie aplikacji:
### 1. Wejdź w folder /29415_52665_52668

### 2. Terminal:

```
python -m venv wirtual
```
```
pip install -r requirements.txt
```
```
python manage.py runserver
```
### 3. Uruchom: http://127.0.0.1:8000/
