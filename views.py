from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User, Teacher, Student, Subject, Class, Schedule, Grade

# -----------------------------
# Головна сторінка
# -----------------------------
def home(request):
    return render(request, 'home.html')  # Простий шаблон із посиланнями

# -----------------------------
# Реєстрація вчителя
# -----------------------------
def register_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        subject_id = request.POST['subject']
        user = User.objects.create_user(username=username, password=password, is_teacher=True)
        subject = Subject.objects.get(id=subject_id)
        Teacher.objects.create(user=user, subject=subject)
        return redirect('home')
    subjects = Subject.objects.all()
    return render(request, 'register_teacher.html', {'subjects': subjects})

# -----------------------------
# Реєстрація учня
# -----------------------------
def register_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        class_id = request.POST['class']
        user = User.objects.create_user(username=username, password=password, is_student=True)
        student_class = Class.objects.get(id=class_id)
        Student.objects.create(user=user, student_class=student_class)
        return redirect('home')
    classes = Class.objects.all()
    return render(request, 'register_student.html', {'classes': classes})

# -----------------------------
# Додати розклад
# -----------------------------
def add_schedule(request):
    if request.method == 'POST':
        subject = Subject.objects.get(id=request.POST['subject'])
        teacher = Teacher.objects.get(id=request.POST['teacher'])
        student_class = Class.objects.get(id=request.POST['class'])
        day = request.POST['day']
        time = request.POST['time']
        Schedule.objects.create(subject=subject, teacher=teacher, student_class=student_class, day=day, time=time)
        return redirect('home')
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    classes = Class.objects.all()
    return render(request, 'add_schedule.html', {'subjects': subjects, 'teachers': teachers, 'classes': classes})

# -----------------------------
# Додати оцінку
# -----------------------------
def add_grade(request):
    if request.method == 'POST':
        student = Student.objects.get(id=request.POST['student'])
        subject = Subject.objects.get(id=request.POST['subject'])
        grade_value = request.POST['grade']
        Grade.objects.create(student=student, subject=subject, grade=grade_value)
        return redirect('home')
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'add_grade.html', {'students': students, 'subjects': subjects})