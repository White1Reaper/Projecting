from django.db import models

class ShortTeacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Teacher(ShortTeacher):
    work_experience = models.IntegerField()
    department = models.CharField(max_length=50)
    group_id = models.IntegerField()
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
