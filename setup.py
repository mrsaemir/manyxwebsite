# one click install python file for the project
import os
import shutil
import sys


def create_dir_in_path(dir_name, path_):
    dir_path = os.path.join(path_, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path


def get_server_ip():
    import socket
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ", host_name)
        print("IP : ", host_ip)
    except:
        print("Unable to get Hostname and IP")
    return host_ip


# call this function on initialization only.
def set_secrets():
    # reading
    with open('/manyx/secret', 'r') as file:
        filedata = file.read()
    # modifiying
    filedata = filedata.replace('some_user', raw_input("\nDataBase Username:\t"))
    filedata = filedata.replace('some_password', raw_input("\nDataBase Password:\t"))
    filedata = filedata.replace('some_db', raw_input("\nDataBase Name:\t"))
    filedata = filedata.replace('top_secret', raw_input("\nSecret Key:\t"))
    filedata = filedata.replace('server_ip', get_server_ip())
    # saving
    with open("/manyx/secret", 'w') as file:
        file.write(filedata)


def deploy():
    # installing required packages
    os.system("apt update ; apt install docker docker.io docker-compose")
    # initializing secret file
    create_dir_in_path("manyx", "/")
    shutil.copy(os.path.join(os.path.abspath(os.path.dirname(__file__)), "secret"), "/manyx/secret")
    # configuring env var files
    set_secrets()
    os.system("docker-compose up --build -d")
    os.system("docker-compose exec web python manage.py migrate --noinput")
    os.system("docker-compose exec web python manage.py collectstatic --noinput")
    os.system("docker-compose down ; docker-compose up -d")


def update():
    os.system("git pull origin master")
    os.system("docker-compose down ; docker-compose up -d --build")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode.lower() == "deploy":
        deploy()
    elif mode.lower() == "update":
        update()

