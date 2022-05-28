run:
				python3 manage.py runserver

shell:
				pipenv shell

migrate:
				python3 manage.py makemigrations images && python3 manage.py migrate