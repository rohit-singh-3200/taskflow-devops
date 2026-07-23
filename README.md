# TaskFlow DevOps Pipeline

A production-ready Flask task management application built to demonstrate modern DevOps practices, including containerization, CI/CD, and cloud deployment.

## Features

- User Authentication
- Password Hashing
- Session Management
- CRUD Operations
- MySQL Database
- Environment Variables
- Responsive UI
- CI/CD Workflow

## Tech Stack

- Python
- Flask
- MySQL
- HTML
- CSS
- Git
- GitHub

## Upcoming

- Docker
- Docker Compose
- GitHub Actions
- AWS EC2 Deployment
- Gunicorn
- Nginx

## Project Structure

```text
.
├── app.py
├── db.py
├── requirements.txt
├── static/
├── templates/
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/rohit-singh-3200/taskflow-devops.git
cd taskflow-devops
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Create a `.env` file in the project root and add the following:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=taskflow

SECRET_KEY=your_secret_key
```

Replace the values with your own MySQL credentials and a secure secret key.

### 4. Create the MySQL database

```sql
CREATE DATABASE taskflow;
```

Import or create the required tables (`users` and `tasks`) before running the application.

### 5. Run the application

```bash
python app.py
```


## License

MIT
