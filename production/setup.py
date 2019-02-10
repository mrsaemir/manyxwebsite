# importing application
import os


def deploy():
    os.system("apt update && apt install -y docker docker.io")
    os.system("docker login")
    os.system("mkdir -p /var/manyx/media")
    os.system("mkdir -p /var/manyx/static")
    os.system("mkdir -p /var/manyx/database")


if "__name__" == "__main__":
    deploy()

