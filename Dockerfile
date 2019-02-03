﻿# start from an official image
FROM python:3.7

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/
RUN pip install pipenv && pipenv install --system

ENV PYTHONUNBUFFERED 1

# copy our project code
COPY . /opt/services/djangoapp/src
RUN cd dana && python manage.py collectstatic --no-input

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "dana", "--bind", ":8000", "dana.wsgi:application"]
