migrate:
	uv run manage.py migrate

start:
	uv run manage.py runserver

worker:
	uv run manage.py db_worker

tailwind:
	uv run manage.py tailwind build
	uv run manage.py tailwind watch

clear:
	uv run manage.py clear_models

seed:
	uv run manage.py seed
