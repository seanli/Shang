#!/bin/bash

git push git@heroku.com:shang.git master
heroku run python manage.py migrate --app shang
heroku run python manage.py collectstatic --noinput --app shang
