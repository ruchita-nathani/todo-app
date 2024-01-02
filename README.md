# Flask To-Do Application

## Overview

This is a simple todo app built using Flask and SQLAlchemy. It allows users to create, read, update, and delete (CRUD) todo items.

## Features
- Add new tasks with a title and description.
- View a list of all tasks.
- Update tasks.
- Delete tasks.

### Prerequisites

- Python
- Flask
- SQLAlchemy

### Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to [http://localhost:8000](http://localhost:8000).

3. Use the app to manage your todo list.

<!-- # Give an execute permission to the script file of app
```[bash]
chmod +x ./todo-app/run_app.sh
```
# Runs the app
```[bash]
chmod ./todo-app/run_app.sh
```

The app will be accessible at http://localhost:8000.

$ flask shell
```[bash]
db.create_all()
```

Or push a context manually if using a plain python shell.

$ python

`from project import app, db`

`app.app_context().push()`

`db.create_all()` -->