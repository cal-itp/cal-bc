start:
	uv run manage.py runserver

tailwind:
	uv run manage.py tailwind build
	uv run manage.py collectstatic
	uv run manage.py tailwind watch
