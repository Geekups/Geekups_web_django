FROM python:latest

RUN mkdir /dayana_blog
WORKDIR /dayana_blog
COPY . /dayana_blog

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input


CMD ["gunicorn", "--chdir", "config", "--bind", ":8000", "config.wsgi:application"]
