# importing application
import os


def pre_deploy():
    os.system("apt update && apt install -y docker docker.io")
    os.system("docker login")
    os.system("mkdir -p /var/manyx/media")
    os.system("mkdir -p /var/manyx/static")
    os.system("mkdir -p /var/manyx/database")


pre_deploy()
