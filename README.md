#cd ~
#cd projects
#django-admin startproject barbican
#mv README.md ./barbican/
#cd barbican/
#python manage.py startapp members
#python manage.py runserver

rhine@Richard-MBP barbican % python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
July 16, 2023 - 15:17:55
Django version 4.2.3, using settings 'barbican.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

#python manage.py makemigrations \
#python manage.py migrate \
#python manage.py createsuperuser \

