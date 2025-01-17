FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# permanent dependencies
RUN apk add --update --no-cache postgresql-client jpeg-dev
# temporary dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

WORKDIR /app
COPY . .

# store media files uploaded by users
RUN mkdir -p /vol/web/media
# store static files
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

CMD sh -c "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:5000"