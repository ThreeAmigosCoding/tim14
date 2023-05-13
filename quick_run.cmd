rem install D3Core
cd D3Core
pip install .
cd ../

cd django_project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver