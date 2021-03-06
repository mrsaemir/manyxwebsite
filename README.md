# MANYX WEBSITE PROJECT
Welcome to Manyx website project which is the official
website for manyx team.

Here are some tips for installing and using manyx project:
- a python3 and django2 project
- designed using django-rest-framework 
- fast development environment setup
- fast deploy friendly
- supporting persian date and time 

## Client/Server Architecture
This project uses api to interact with client side

- Client side is written using vue.js by **Sajjad Hadi**
- Server side is written using django/python by **Amirhossein Saemi**

## Supporting Jalali Date and Time
Iranian date and time is used in this project for more language and culture 
compatibility.

## Fast development environment 
This project uses docker-compose to rapidly create suitable environment for development purpose.
If you are a developer and want to work on the project. just type **docker-compose up**
to setup a full development environment in a second.
#### NOTE : the default superuser for testing purposes is "admin" with password "adminadmin"
 
## Deploy Guide
- pull the project to your server using git
- cd /production
- bring all the past files if needed.
- run python setup.py (for pre_setup configs)
- activate swarm and join all the workers and managers
- configure production.yaml for project settings.
- run docker stack deploy -c production.yaml <service-name> --with-registry-auth
