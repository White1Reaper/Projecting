import json
import re
from models.short_teacher import ShortTeacher

class Teacher(ShortTeacher):
    def __init__(self, teacher_id, name, surname, patronymic, phone, work_experience, department, group_id):
        super().__init__(teacher_id, name, surname, patronymic)
        self.phone = phone
        self.work_experience = work_experience
        self.department = department
        self.group_id = group_id

    def ser_obj(self):
        return {
            'teacher_id': self.teacher_id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,
            'phone': self.phone,
            'work_experience': self.work_experience,
            'department': self.department,
            'group_id': self.group_id
        }

    @staticmethod
    def val_phone(phone):
        return bool(re.match(r'^(\+?7|8)\d{3}\d{3}\d{2}\d{2}$', phone))

    @staticmethod
    def val_work_experience(work_experience):
        return isinstance(work_experience, int) and work_experience >= 0

    @staticmethod
    def val_department(department):
        return isinstance(department, str) and bool(department.strip())

    @staticmethod
    def val_group_id(group_id):
        return isinstance(group_id, int) and group_id > 0

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}, Phone: {self.phone}, Work Experience: {self.work_experience}, Department: {self.department}, Group ID: {self.group_id}"
