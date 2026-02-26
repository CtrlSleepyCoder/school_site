from flask import Flask, render_template_string, request, redirect
import data
from templates import layout

app = Flask(__name__)

# -----------------------------
# Головна сторінка
# -----------------------------
@app.route("/")
def home():
    content = "<div class='card'><h2>Ласкаво просимо!</h2><p>Виберіть опцію з меню зверху.</p></div>"
    return render_template_string(layout(content))

# -----------------------------
# Додати предмет
# -----------------------------
@app.route("/add_subject", methods=["GET", "POST"])
def add_subject():
    if request.method == "POST":
        name = request.form["name"]
        data.subjects.append({"id": len(data.subjects)+1, "name": name})
        return redirect("/add_subject")
    content = """
    <div class='card'>
    <h2>Додати предмет</h2>
    <form method='post'>
        Назва: <input name='name' required><br>
        <button>Додати</button>
    </form>
    </div>
    """
    return render_template_string(layout(content))

# -----------------------------
# Додати клас
# -----------------------------
@app.route("/add_class", methods=["GET", "POST"])
def add_class():
    if request.method == "POST":
        name = request.form["name"]
        data.classes.append({"id": len(data.classes)+1, "name": name})
        return redirect("/add_class")
    content = """
    <div class='card'>
    <h2>Додати клас</h2>
    <form method='post'>
        Назва: <input name='name' required><br>
        <button>Додати</button>
    </form>
    </div>
    """
    return render_template_string(layout(content))

# -----------------------------
# Реєстрація вчителя
# -----------------------------
@app.route("/register_teacher", methods=["GET","POST"])
def register_teacher():
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        subject_id = int(request.form["subject"])
        data.users.append({"username":username,"password":password,"role":"teacher"})
        data.teachers.append({"username":username,"subject_id":subject_id})
        return redirect("/register_teacher")
    options = "".join([f"<option value='{s['id']}'>{s['name']}</option>" for s in data.subjects])
    content = f"""
    <div class='card'>
    <h2>Реєстрація вчителя</h2>
    <form method='post'>
        Ім'я: <input name='username' required><br>
        Пароль: <input type='password' name='password' required><br>
        Предмет: <select name='subject'>{options}</select><br>
        <button>Зареєструвати</button>
    </form>
    </div>
    """
    return render_template_string(layout(content))

# -----------------------------
# Реєстрація учня
# -----------------------------
@app.route("/register_student", methods=["GET","POST"])
def register_student():
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        class_id = int(request.form["class"])
        data.users.append({"username":username,"password":password,"role":"student"})
        data.students.append({"username":username,"class_id":class_id})
        return redirect("/register_student")
    options = "".join([f"<option value='{c['id']}'>{c['name']}</option>" for c in data.classes])
    content = f"""
    <div class='card'>
    <h2>Реєстрація учня</h2>
    <form method='post'>
        Ім'я: <input name='username' required><br>
        Пароль: <input type='password' name='password' required><br>
        Клас: <select name='class'>{options}</select><br>
        <button>Зареєструвати</button>
    </form>
    </div>
    """
    return render_template_string(layout(content))

# -----------------------------
# Додати розклад
# -----------------------------
@app.route("/add_schedule", methods=["GET","POST"])
def add_schedule():
    if request.method=="POST":
        subject_id = int(request.form["subject"])
        teacher_username = request.form["teacher"]
        class_id = int(request.form["class"])
        day = request.form["day"]
        time = request.form["time"]
        data.schedules.append({"subject_id":subject_id,"teacher_username":teacher_username,"class_id":class_id,"day":day,"time":time})
        return redirect("/add_schedule")
    subject_options = "".join([f"<option value='{s['id']}'>{s['name']}</option>" for s in data.subjects])
    teacher_options = "".join([f"<option value='{t['username']}'>{t['username']}</option>" for t in data.teachers])
    class_options = "".join([f"<option value='{c['id']}'>{c['name']}</option>" for c in data.classes])
    content = f"""
    <div class='card'>
    <h2>Додати розклад</h2>
    <form method='post'>
        Предмет: <select name='subject'>{subject_options}</select><br>
        Вчитель: <select name='teacher'>{teacher_options}</select><br>
        Клас: <select name='class'>{class_options}</select><br>
        День: <input name='day' required><br>
        Час: <input name='time' required><br>
        <button>Додати</button>
    </form>
    </div>
    """
    return render_template_string(layout(content))

# -----------------------------
# Додати оцінку
# -----------------------------
@app.route("/add_grade", methods=["GET","POST"])
def add_grade():
    if request.method=="POST":
        student_username = request.form["student"]
        subject_id = int(request.form["subject"])
        grade_value = request.form["grade"]
        data.grades.append({"student_username":student_username,"subject_id":subject_id,"grade":grade_value})
        return redirect("/add_grade")
    student_options = "".join([f"<option value='{s['username']}'>{s['username']}</option>" for s in data.students])
    subject_options = "".join([f"<option value='{s['id']}'>{s['name']}</option>" for s in data.subjects])
    content = f"""
    <div class='card'>
    <h2>Додати оцінку</h2>
    <form method='post'>
        Учень: <select name='student'>{student_options}</select><br>
        Предмет: <select name='subject'>{subject_options}</select><br>
        Оцінка: <input name='grade' required><br>
        <button>Додати</button>
    </form>
    </div>
    """
    return render_template_string(layout(content))

# -----------------------------
# Перегляд даних
# -----------------------------
@app.route("/view")
def view_data():
    content = "<div class='card'><h2>Всі дані</h2>"
    content += "<h3>Предмети:</h3><ul>" + "".join([f"<li>{s['name']}</li>" for s in data.subjects]) + "</ul>"
    content += "<h3>Класи:</h3><ul>" + "".join([f"<li>{c['name']}</li>" for c in data.classes]) + "</ul>"
    content += "<h3>Вчителі:</h3><ul>" + "".join([f"<li>{t['username']} - {data.subjects[t['subject_id']-1]['name']}</li>" for t in data.teachers]) + "</ul>"
    content += "<h3>Учні:</h3><ul>" + "".join([f"<li>{s['username']} - {data.classes[s['class_id']-1]['name']}</li>" for s in data.students]) + "</ul>"
    content += "<h3>Розклад:</h3><ul>" + "".join([f"<li>{data.subjects[r['subject_id']-1]['name']} | {r['teacher_username']} | {data.classes[r['class_id']-1]['name']} | {r['day']} {r['time']}</li>" for r in data.schedules]) + "</ul>"
    content += "<h3>Оцінки:</h3><ul>" + "".join([f"<li>{g['student_username']} | {data.subjects[g['subject_id']-1]['name']} | {g['grade']}</li>" for g in data.grades]) + "</ul>"
    content += "</div>"
    return render_template_string(layout(content))

# -----------------------------
# Запуск сервера
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)