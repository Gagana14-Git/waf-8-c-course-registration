from flask import Flask, request, render_template_string

app = Flask(__name__)
registrations = []

courses = [
    "Python Programming",
    "Web Development",
    "Machine Learning",
    "Database Management"
]

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form["name"].strip()
        course = request.form["course"]

        if name:
            registrations.append({
                "name": name,
                "course": course
            })
            message = "Registration successful!"

    return render_template_string("""
    <h2>Online Student Course Registration System</h2>

    <form method="POST">
        Student Name:
        <input type="text" name="name" required>

        <br><br>

        Select Course:
        <select name="course">
            {% for course in courses %}
                <option value="{{ course }}">{{ course }}</option>
            {% endfor %}
        </select>

        <br><br>
        <button type="submit">Register</button>
    </form>

    <p>{{ message }}</p>

    <h3>Registered Students</h3>
    {% for student in registrations %}
        <p>{{ student.name }} - {{ student.course }}</p>
    {% endfor %}
    """, courses=courses, registrations=registrations, message=message)

if __name__ == "__main__":
    app.run(debug=True)

