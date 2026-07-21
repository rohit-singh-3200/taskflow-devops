from flask import Flask, session, render_template, request, flash, redirect, url_for
from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
def home():
    if "user_id" in session:
        return redirect(url_for("tasks"))

    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("tasks"))
    
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = None
        cursor = None

        try:
            connection = get_db()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT * FROM users WHERE username = %s",
                (username,)
            )

            user = cursor.fetchone()

            if user is None:
                flash("User not found.", "error")

            elif check_password_hash(user[2], password):

                session["user_id"] = user[0]
                session["username"] = user[1]

                flash("Login successful!", "success")
                return redirect(url_for("tasks"))

            else:
                flash("Incorrect password.", "error")

        except Exception as e:
            print(e)
            flash("Login failed.", "error")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():

    if "user_id" in session:
        return redirect(url_for("tasks"))

    if request.method == "POST":
    
        username=request.form["username"]
        password=request.form["password"]
        confirm_password=request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match","error")
        else:
            connection = None
            cursor = None
            try:
                connection = get_db()
                cursor = connection.cursor()
                hashed_password = generate_password_hash(password)
                cursor.execute(
                    "INSERT INTO users (username,password) VALUES (%s, %s)",
                    (username,hashed_password)
                )
                connection.commit()

                flash("Registration successful!", "success")
                return redirect(url_for("login"))
            
            except Exception as e:
                print(e)
                flash("Registration failed.","error")
            
            finally:
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
    return render_template('register.html')

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
        
    if "user_id" not in session:
        flash("Please login first.", "error")
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form["title"]

        connection = None
        cursor = None

        try:
            connection = get_db()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO tasks (user_id, title) VALUES (%s, %s)",
                (session["user_id"], title)
            )

            connection.commit()

            flash("Task added successfully!", "success")

        except Exception as e:
            print(e)
            flash("Failed to add task.", "error")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    # Fetch all tasks
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks WHERE user_id = %s ORDER BY created_at DESC",
    (session["user_id"],))

    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "tasks.html",
        tasks=tasks,
        username=session.get("username")
    )

@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    connection = None
    cursor = None

    try:
        connection = get_db()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM tasks WHERE id = %s",
            (task_id,)
        )

        connection.commit()

        flash("Task deleted successfully!", "success")

    except Exception as e:
        print(e)
        flash("Failed to delete task.", "error")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return redirect(url_for("tasks"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):

    connection = None
    cursor = None

    try:
        connection = get_db()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE tasks SET completed = TRUE WHERE id = %s",
            (task_id,)
        )

        connection.commit()

        flash("Task completed!", "success")

    except Exception as e:
        print(e)
        flash("Failed to complete task.", "error")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return redirect(url_for("tasks"))

@app.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully!", "success")

    return redirect(url_for("home"))

if __name__=='__main__':
    app.run(debug=True)