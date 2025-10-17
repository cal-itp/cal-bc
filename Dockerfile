# Use the official Python runtime image
FROM python:3.13

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.9.3 /uv /uvx /bin/

# Create the app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Set environment variables
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Copy the Django project to the container
COPY . /app/

# Sync the project into a new environment, asserting the lockfile is up to date
RUN uv sync --locked

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]
