from django.db import models


# -----------------------------
# МОДЕЛЬ ПРЕДМЕТ (Uroks)
# -----------------------------
class Uroks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# -----------------------------
# МОДЕЛЬ ВЧИТЕЛЬ
# -----------------------------
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(
        Uroks,
        on_delete=models.CASCADE,
        related_name="teachers"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# -----------------------------
# МОДЕЛЬ КЛАС
# -----------------------------
class Class(models.Model):
    name = models.CharField(max_length=20)  # Наприклад: 10-A
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"


# -----------------------------
# МОДЕЛЬ УЧЕНЬ
# -----------------------------
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school_class = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# -----------------------------
# МОДЕЛЬ РОЗКЛАД
# -----------------------------
class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
    ]

    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    lesson_number = models.IntegerField()

    subject = models.ForeignKey(
        Uroks,
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    school_class = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    def __str__(self):
        return f"{self.day} - Lesson {self.lesson_number}"


# -----------------------------
# МОДЕЛЬ ОЦІНКА
# -----------------------------
class Grade(models.Model):
    value = models.IntegerField()

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="grades"
    )

    subject = models.ForeignKey(
        Uroks,
        on_delete=models.CASCADE,
        related_name="grades"
    )

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.value}"