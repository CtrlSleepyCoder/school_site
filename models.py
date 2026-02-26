from django.db import models
from django.contrib.auth.models import AbstractUser

# -----------------------------
# Користувач: розширюємо AbstractUser
# -----------------------------
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

# -----------------------------
# Предмети
# -----------------------------
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# -----------------------------
# Класи
# -----------------------------
class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# -----------------------------
# Вчителі
# -----------------------------
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# -----------------------------
# Учні
# -----------------------------
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# -----------------------------
# Розклад
# -----------------------------
class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)   # Наприклад "Понеділок"
    time = models.CharField(max_length=20)  # Наприклад "9:00-10:00"

    def __str__(self):
        return f"{self.subject} - {self.student_class} - {self.day} {self.time}"

# -----------------------------
# Оцінки
# -----------------------------
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)  # Наприклад "A", "B+", "12/12"

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade}"