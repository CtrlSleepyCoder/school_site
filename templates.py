# templates.py
def layout(content):
    return f"""
<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>Шкільна система</title>
<style>
body {{ font-family: 'Segoe UI', sans-serif; background: #f4f6f8; margin:0; padding:0;}}
header {{ background: #4CAF50; color: white; padding: 20px; text-align: center;}}
nav {{ background: #fff; padding: 10px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);}}
nav a {{ margin: 0 10px; color: #4CAF50; text-decoration: none; font-weight: bold;}}
nav a:hover {{ text-decoration: underline;}}
.container {{ max-width: 900px; margin: 20px auto; padding: 10px;}}
.card {{ background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.15); margin-bottom: 20px;}}
input, select, button {{ width: 100%; padding: 8px; margin: 6px 0 12px 0; border-radius: 5px; border: 1px solid #ccc;}}
button {{ background: #4CAF50; color: white; border: none; cursor: pointer; font-weight: bold;}}
button:hover {{ background: #45a049;}}
table {{ width: 100%; border-collapse: collapse;}}
th, td {{ padding: 8px; text-align: left; border-bottom: 1px solid #ddd;}}
th {{ background: #f2f2f2;}}
</style>
</head>
<body>
<header><h1>Система керування школою</h1></header>
<nav>
<a href="/">Головна</a>
<a href="/add_subject">Предмети</a>
<a href="/add_class">Класи</a>
<a href="/register_teacher">Вчителі</a>
<a href="/register_student">Учні</a>
<a href="/add_schedule">Розклад</a>
<a href="/add_grade">Оцінки</a>
<a href="/view">Перегляд даних</a>
</nav>
<div class="container">
{content}
</div>
</body>
</html>
"""