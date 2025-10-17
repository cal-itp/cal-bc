#!/usr/bin/env bash

uv run --no-sync manage.py migrate
uv run --no-sync manage.py collectstatic
uv run --no-sync manage.py tailwind build
uv run --no-sync manage.py runserver 0.0.0.0:8000
