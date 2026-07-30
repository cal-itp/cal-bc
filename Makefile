start:
	uv run manage.py runserver

worker:
	uv run manage.py db_worker

tailwind:
	uv run manage.py tailwind build
	uv run manage.py collectstatic
	uv run manage.py tailwind watch
