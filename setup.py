# one click install python file for the project
import os
import shutil


def create_dir_in_path(dir_name, path_):
    dir_path = os.path.join(path_, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path


def deploy():
    # installing required packages
    os.system("apt update ; apt install docker docker.io docker-compose")
    # initializing secret file
    create_dir_in_path("manyx", "/")
    shutil.copy("./sceret", "/")
    os.system("docker-compose up --build -d")
    os.system("docker-compose exec web python manage.py migrate --noinput")
    os.system("docker-compose exec web python manage.py collectstatic --noinput")
    os.system()
    os.system("docker-compose down ; docker-compose up -d")


def update():
    os.system("git pull origin master")
    os.system("docker-compose down ; docker-compose up -d --build")