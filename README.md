# todo-app

$ flask shell
>>> db.create_all()
Or push a context manually if using a plain python shell.

$ python
>>> from project import app, db
>>> app.app_context().push()
>>> db.create_all()