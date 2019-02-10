# importing application
import os


def pre_deploy():
    os.system("apt update && apt install -y docker docker.io")
    os.system("docker login")
    os.system("mkdir -p /var/manyx/media")
    os.system("mkdir -p /var/manyx/static")
    os.system("mkdir -p /var/manyx/database")
    os.system("""echo NOTICE: you have to manually initial your swarm,
                 edit your production.yaml file and join all the clusters
                  to your manager node""")


if "__name__" == "__main__":
    pre_deploy()

