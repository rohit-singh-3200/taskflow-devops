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
- Dockerized Application
- CI/CD Pipeline
- AWS EC2 Deployment

---

## Tech Stack

- Python
- Flask
- MySQL
- HTML
- CSS
- Git
- GitHub
- Docker
- Docker Compose
- GitHub Actions
- AWS EC2

---

## Upcoming

- Gunicorn
- Nginx

---

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── db.py
├── docker-compose.yml
├── docker-compose.prod.yml
├── Dockerfile
├── mysql/
├── static/
├── templates/
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/rohit-singh-3200/taskflow-devops.git
cd taskflow-devops
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create a `.env` file

Create a `.env` file in the project root and add the following variables:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=taskflow

SECRET_KEY=your_secret_key
```

Replace the placeholder values with your own MySQL credentials and a secure secret key.

---

## 4. Create the MySQL database

```sql
CREATE DATABASE taskflow;
```

Import or create the required tables (`users` and `tasks`) before running the application.

---

## 5. Run the application

```bash
python app.py
```

---

# Docker Deployment

Build and start the containers:

```bash
docker compose up --build
```

---

# CI/CD Deployment

To enable automated deployment using GitHub Actions:

1. Create the required GitHub repository secrets.
2. Refer to `.github/workflows/ci.yml` for the complete list of required secret names.
3. Create a `.env` file on your EC2 instance containing the required environment variables before deploying.

Example `.env` for production:

```env
DB_HOST=mysql
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=taskflow

MYSQL_ROOT_PASSWORD=your_mysql_root_password

SECRET_KEY=your_secret_key
```

After configuring the secrets and the `.env` file, every push to the `main` branch will automatically build the Docker image, push it to Docker Hub, and deploy the latest version to the EC2 instance.

---

## License

MIT
