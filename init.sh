python -m venv project-venv
pip install -r requirements.txt
python3 manage.py makemigrations course
python3 manage.py makemigrations instructor
python3 manage.py makemigrations TA
python3 manage.py migrate
python3 manage.py runserver