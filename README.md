Happy New Year 2026 — Django Application
python -m venv venv
source venv/bin/activate # on Windows: venv\Scripts\activate
pip install django


# create project and app
django-admin startproject mysite
cd mysite
python manage.py startapp newyear


# add 'newyear' to INSTALLED_APPS in mysite/settings.py
 then make migrations and run
 python manage.py runserver
 Project structure (important files shown)
 mysite/
├── mysite/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── newyear/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
│ ├── admin.py
│ ├── templates/newyear/index.html
│ └── static/newyear/ (css, js, images)
└── manage.py
Quick next steps you can follow now:

Open the canvas document and copy the files into your mysite/newyear/ app.

Add 'newyear' to INSTALLED_APPS in mysite/settings.py.

Put a wallpaper image at static/newyear/images/newyear_wallpaper.jpg.

Run python manage.py makemigrations && python manage.py migrate and then python manage.py runserver.

Want me to:

export the static files and templates as downloadable files now, 

host urls = https://www.pythonanywhere.com/user/saideepak/consoles/42968889/
