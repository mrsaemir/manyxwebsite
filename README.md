# MANYX WEBSITE PROJECT
Welcome to Manyx website project which is the official
website for manyx team.

Here are some tips for installing and using manyx project:
- a python3 and django2 project
- designed using django-rest-framework 
- fast deploy friendly
- supporting persian date and time 

## Client/Server Architecture
This project uses api to interact with client side

- Client side is written using vue.js by **Sajjad Hadi**
- Server side is written using django/python by **Amirhossein Saemi**

## Fast Deploy 
All the project is designed in a way that can run on any machine as quickly as possible.

## Supporting Jalali Date and Time
Iranian date and time is used in this project for more language and culture 
compatibility.

# Installation and Deploy CheckList:
    0  Clone the project from the repository. 
        Note: In order to user gitlab.com, you have to change your dns.
        ( a good dns provider would be http://shecan.ir )
    
    1  Install apache with mod_wsgi:
        - sudo apt-get install python3-pip
        - sudo apt-get install apache2
        - sudo apt-get install libapache2-mod-wsgi-py3
    
    2  Install postgresql:
        - sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
    
    3  Create virtualenv(Python 3.5).:
        - sudo pip3 install virtualenv
        - virtualenv -p Python3.5 <env-name>
        - source <env-name>/bin/activate
         
    4  Install requiremenst(in your env).:
        - pip3 install -r requirements.txt
        
    5  Configure apache2.
        - go to /etc/apache2/sites-available.
        - open the default .conf file and fill it like the example.
    
    6  Configure the project to run on the server:
        - set .bashrc in case of using the project(put bashrc's content in apache envvar file and ~/.bashrc).
        - make the migrations and migrate.
    
    7  Restart apache2.
        - sudo service apache2 restart
        
    8  Restart server.
        - sudo reboot
         
   **Note**: a sample for .bashrc is available in this package.
   **Note** : a sample for /etc/apache2/sites-available is available in this package.
    
