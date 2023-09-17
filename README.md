# Task Manager with REST API

**Project Description:**

A web application for managing tasks with a REST API using Django. This project allows multiple users to create, view, update, and delete tasks, utilizing Django templates for rendering views, PostgreSQL for the database, and Django ORM for managing database relations. 


## Features
Task creation, update, deletion.
Task listing with filtering and searching.
Priority levels for tasks.
Mark tasks as complete.
Task due dates.
User authentication in Admin panel.
API endpoints for task management.


## Project Setup

### Django Project Setup

1. Clone this repository: https://github.com/br25/task_manager.git
2. Open Two Terminal:
    * First Terminal: docker-compose up
    * Second Terminal: 
    - docker-compose exec web pip install -r requirements.txt

    - docker-compose exec web python manage.py makemigrations

    - docker-compose exec web python manage.py migrate

    - docker-compose exec web python manage.py createsuperuser

    - docker-compose exec web python mana
    ge.py loaddata users.json

    - docker-compose exec web python mana
    ge.py loaddata tasks.json
    
    - docker-compose exec web python mana
    ge.py loaddata photos.json
    
    - docker-compose exec web python manage.py runserver 0.0.0.0:8000

3. If not Docker:
    1. Clone this repository.
    2. Create a virtual environment for the project: `virtualenv venv` (optional but recommended).
    3. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows).
    4. Install project dependencies: `pip install -r requirements.txt`.
    5. Fixtures: `python manage.py loaddata` ( users.json, tasks.json, photos.json )

    6. Migrations: `python manage.py`(makemigrations, migrate, runserver).


## API Endpoints

### Task Class-based API Endpoints

- **List Tasks:**  
  - Endpoint: `/tasks/`
  - View: `TaskListAPIView`
  - Description: Lists all tasks.
  
- **Create Task:**  
  - Endpoint: `/tasks/create/`
  - View: `TaskCreateAPIView`
  - Description: Creates a new task.
  
- **Task Details:**  
  - Endpoint: `/tasks/<int:pk>/`
  - View: `TaskDetailAPIView`
  - Description: Retrieves details of a specific task by its primary key (`pk`).
  
- **Update Task:**  
  - Endpoint: `/tasks/<int:pk>/update/`
  - View: `TaskUpdateAPIView`
  - Description: Updates an existing task by its primary key (`pk`).
  
- **Delete Task:**  
  - Endpoint: `/tasks/<int:pk>/delete/`
  - View: `TaskDeleteAPIView`
  - Description: Deletes an existing task by its primary key (`pk`).

### Photos Class-based API Endpoints

- **List and Create Photos:**  
  - Endpoint: `/photos/`
  - View: `PhotoListCreateView`
  - Description: Lists photos and allows creating new photos.
  
- **Photo Details:**  
  - Endpoint: `/photos/<int:pk>/`
  - View: `PhotoDetailView`
  - Description: Retrieves details of a specific photo by its primary key (`pk`).

### Task Function-based API Endpoints

- **List Tasks (Function-based View):**  
  - Endpoint: `/`
  - View: `task_list`
  - Description: Lists all tasks using a function-based view.
  
- **Create Task (Function-based View):**  
  - Endpoint: `/create/`
  - View: `task_create`
  - Description: Creates a new task using a function-based view.
  
- **Task Details (Function-based View):**  
  - Endpoint: `/<int:pk>/`
  - View: `task_detail`
  - Description: Retrieves details of a specific task by its primary key (`pk`) using a function-based view.
  
- **Update Task (Function-based View):**  
  - Endpoint: `/<int:pk>/update/`
  - View: `task_update`
  - Description: Updates an existing task by its primary key (`pk`) using a function-based view.
  
- **Delete Task (Function-based View):**  
  - Endpoint: `/<int:pk>/delete/`
  - View: `task_delete`
  - Description: Deletes an existing task by its primary key (`pk`) using a function-based view.
