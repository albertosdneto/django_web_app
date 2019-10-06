# django_web_app

## Screenshots

| Column A                        | Column B                     |
|---------------------------------|------------------------------|
| ![Home](screenshots/01.png)     | ![Login](screenshots/02.png) |
| ![Register](screenshots/03.png) | ![User](screenshots/04.png)  |

## About

Building a web app with Django based on the tutorial series by  Corey Schafer that can be found at the link below.

- <https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p>


## Installation

- Create a virtual environment with python 3.6. In my case I used conda for that.
```shell
conda create -n blogEnv python=3.6
```
- Activate the virtual environment you have just created:
```shell
conda activate blogEnv
```
- Clone the repository:
```shell
git clone https://github.com/albertosdneto/django_web_app.git
```
- Go to the django_project folder and install the requirements:
```shell
cd django_web_app

cd django_project

pip install -r requirements.txt
```
- Setup environment variables or setup these values inside ```settings.py```:
``` python
SECRET_KEY = "#####################"
EMAIL_USER = "#####################"
EMAIL_PASSWORD = "#####################"
```
- Migrate database:
```shell
python manage.py makemigrations
python manage.py migrate
```
- Create Superuser:
```shell
python manage.py createsuperuser
```
- Run the project:
```shell
python manage.py runserver
```
- Go to the project url and verify if it is running. Enjoy.
