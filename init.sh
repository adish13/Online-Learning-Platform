rm -r course/__pycache__
rm -r course/migrations
rm -r instructor/__pycache__
rm -r instructor/migrations
rm -r TA/__pycache__
rm -r TA/migrations
rm db.sqlite3
python3 manage.py makemigrations course
python3 manage.py makemigrations instructor
python3 manage.py makemigrations TA
python3 manage.py migrate
python3 manage.py runserver