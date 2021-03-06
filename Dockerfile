FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# collect static files
RUN python manage.py collectstatic --noinput


# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
# run gunicorn
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT