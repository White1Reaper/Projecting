from django import forms
from .models import Teacher
import re

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'patronymic', 'phone', 'work_experience', 'department', 'group_id']

    def clean_teacher_id(self):
        teacher_id = self.cleaned_data.get('teacher_id')
        if not isinstance(teacher_id, int) or teacher_id <= 0:
            raise forms.ValidationError("Ошибка ID.")
        return teacher_id

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not isinstance(name, str) or not name.strip():
            raise forms.ValidationError("Ошибка ввода имени")
        return name

    def clean_surname(self):
        surname = self.cleaned_data.get('surname')
        if not isinstance(surname, str) or not surname.strip():
            raise forms.ValidationError("Ошибка ввода фамилии")
        return surname

    def clean_patronymic(self):
        patronymic = self.cleaned_data.get('patronymic')
        if not isinstance(patronymic, str) or not patronymic.strip():
            raise forms.ValidationError("Ошибка ввода отчества ")
        return patronymic

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^(\+?7|8)\d{3}\d{3}\d{2}\d{2}$', phone):
            raise forms.ValidationError("Ошибка ввода телефона")
        return phone

    def clean_work_experience(self):
        work_experience = self.cleaned_data.get('work_experience')
        if not isinstance(work_experience, int) or work_experience < 0:
            raise forms.ValidationError("Ошибка ввода стажа")
        return work_experience

    def clean_department(self):
        department = self.cleaned_data.get('department')
        if not isinstance(department, str) or not department.strip():
            raise forms.ValidationError("Ошибка ввода кафедры ")
        return department

    def clean_group_id(self):
        group_id = self.cleaned_data.get('group_id')
        if not isinstance(group_id, int) or group_id <= 0:
            raise forms.ValidationError("Ошибка ввода ID группы")
        return group_id

