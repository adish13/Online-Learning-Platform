# BruteForces_float_moodle
Steps to install virtual environment and get the website running : 

```
python -m venv project-venv
source project-venv/bin/activate
pip install -r requirements.txt 
```
After this :
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
