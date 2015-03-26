virtualenv env

cd env

. bin/activate

git clone https://github.com/SevenKeys/Django-REST-Framework-Backbone-RequireJS.git

cd Django-REST-Framework-Backbone-RequireJS

pip install -r requirements.txt

./manage.py syncdb

./manage.py runserver

127.0.0.1:8000
