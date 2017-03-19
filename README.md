Simple TODO app
========
Version 1.0 - Sun 5 Mar 2017

by Michał Osak

Introduction
------------

Simple TODO app is todo app (web version) sqlite powered

Installation and Requirements
-------------

1. Required modules:
+ Python => 3
+ Flask
+ pip3
+ SQLAlchemy (sudo pip install flask_sqlalchemy
              sudo pip install sqlalchemy)

2. If Flask is installed correctly. You need only run: "python3 main.py" 
   
+ the application will greet you on http://localhost:5000/
   
3. If Flask won't run.
 
+ "export FLASK_APP=main"
+ "flask run"
+ the application will greet you on http://localhost:5000/

Application
----------

Folders:
+ static: css, js, fonts
+ templates: index.html (body), header.html (header), footer.html (footer), ajaxKit.html (ajax responses)

Models:
+ todo class (methods on todolist)

Ajax:
+ url for ajax resonse /ajaxKit/<action> (adding new actions in main.py) 
+ adding new actions js in file static/js/scripts.js

	
	