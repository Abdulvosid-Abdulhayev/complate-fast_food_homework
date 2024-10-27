from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User modeli
class User(AbstractUser):
    USER_ROLES = (
        ('student', 'Student'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    
    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Use a unique related_name here
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Use a unique related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.name

# Teacher modeli
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField('Subject')  # O'qituvchining predmeti
    salary_per_student = models.DecimalField(max_digits=10, decimal_places=2)  # Har bir o'quvchi uchun ish haqi

    def __str__(self):
        return self.name

# Group modeli (foydalanuvchi guruhlari)
class Group(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)  # Guruhning kursi

    def __str__(self):
        return self.name

# Course modeli (kurslar)
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

# Subject modeli (predmetlar)
class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Predmet qaysi kursga tegishli

    def __str__(self):
        return f'{self.name} ({self.course.name})'
