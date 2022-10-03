1) Create virtual env
2) django-admin startapp setup in CLI
3) python manage.py startapp chatapp in CLI
4) Setup.py --> add your chatapp in Installed Apps
5) Tempaltes dir in chatapp dir --> Chatapp-->templates --> chatapp -->index.html
6) Boiler plate in the index.html
7) In Views.py create a function that will open the index.html
8) Create urls.py in chatapp
9) Setup --> include urls that are in use
10) runserver



##################################################
0) pip install channels
1) Initializing asgi.py with scope and events. Scopes hold events in them, they are open until the session is closed or timed-out. Events are things like eg. receive_message, send_message 
2) 