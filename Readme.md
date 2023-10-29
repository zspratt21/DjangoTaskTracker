# Task Tracker API
An API for tracking tasks, built using Django.
## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Running the tests](#running-the-tests)
- [Made With](#made-with)
## Getting Started
These instructions will get you a copy of the project up and running on your local machine.
### Prerequisites
- Python 3.11
- Docker
- An API client such as ARC or Postman
### Installation
1. Using your terminal or IDE of choice, clone the repository:
```bash
git clone https://github.com/zspratt21/DjangoTaskTracker.git
```
2. Navigate into the project folder in a terminal or your IDE of choice, create a copy of env.example and rename it to .env:
```bash
cp env.example .env
```
3. After navigating into the project folder on your system or opening the project in your IDE, start the docker containers:
```bash
docker-compose up -d
```
4. Run the migrations:
```bash
docker-compose exec python-web python manage.py migrate App
```
### Usage
Use an API client such as ARC or Postman, to make requests to the API. By default, the API is hosted at http://localhost:8000. The following endpoints are available:
#### GET /api/Tasks/
Returns a list of all tasks.
#### GET /api/Tasks/{id}/
Returns a single task with the specified id.
#### POST /api/Tasks/
Creates a new task. The request body should contain a JSON object with the following properties:
- name (string)
- isCompleted (bool)
#### PUT /api/Tasks/{id}/
Updates an existing task with the specified id. The request body should contain a JSON object with the following properties:
- id (int)
- name (string)
- isCompleted (bool)
#### DELETE /api/Tasks/{id}/
Deletes an existing task with the specified id.
### Running the tests
Connect your IDE to the testing container or run the tests in the web container:
```bash
docker-compose exec python-web python manage.py test
```
### Made With
[Python](https://www.python.org/)  
[Django](https://www.djangoproject.com/)  
[Django Rest Framework](https://www.django-rest-framework.org/)  
[Tailwind CSS](https://tailwindcss.com/)  
[Docker](https://www.docker.com/) via [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)  
[JetBrains Pycharm](https://www.jetbrains.com/pycharm/)
