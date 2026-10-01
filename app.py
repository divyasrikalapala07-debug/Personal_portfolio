from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database
def init_db():
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            technology TEXT NOT NULL,
            link TEXT
        )
    """)

    # Add sample projects only if database is empty
    cursor.execute("SELECT COUNT(*) FROM projects")

    if cursor.fetchone()[0] == 0:
        projects = [
            (
                "Task Management Application",
                "A web application for creating, updating and tracking tasks.",
                "HTML, CSS, JavaScript",
                "#"
            ),
            (
                "Personal Portfolio Website",
                "A portfolio website to showcase my skills and projects.",
                "HTML, CSS, JavaScript, Flask, SQLite",
                "#"
            )
        ]

        cursor.executemany("""
            INSERT INTO projects
            (title, description, technology, link)
            VALUES (?, ?, ?, ?)
        """, projects)

    conn.commit()
    conn.close()


# Home page
@app.route("/")
def home():

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        projects=projects
    )


# Contact form
@app.route("/contact", methods=["POST"])
def contact():

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return """
    <h2>Thank you for contacting me!</h2>
    <p>Your message has been received.</p>
    <a href="/">Go Back</a>
    """


if __name__ == "__main__":
    init_db()
    app.run(debug=True)