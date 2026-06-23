run_server:
	uv run manage.py runserver

run_tailwind:
	uv run manage.py tailwind build
	uv run manage.py collectstatic
	uv run manage.py tailwind watch
