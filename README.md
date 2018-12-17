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

# Installation and Deploy CheckList (Auto Deploy Using Docker):
    # a list of env vars required by the project is listed in bashrc for non docker installation. 
    0  Clone the project from the repository. 
        Note: In order to user gitlab.com, you have to change your dns.
        ( a good dns provider would be http://shecan.ir )
    
    1 - First Deploy: 
        - install git
        - go to project directory
        - run python setup.py deploy
    2 - Updating Source Code:
        - go to project directory
        - run python setup.py update