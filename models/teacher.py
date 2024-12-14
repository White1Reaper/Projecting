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
    def from_string(cls, s):
        data = s.split(" ")
        if data[0].isdigit():
            teacher_id = int(data[0])
            name = data[1]
            surname = data[2]
            patronymic = data[3]
            phone = data[4]
            work_experience = int(data[5])
            department = data[6]
            group_id = int(data[7])
            return cls(teacher_id, name, surname, patronymic, phone, work_experience, department, group_id)
        else:
            teacher_id = 1
            name = data[0]
            surname = data[1]
            patronymic = data[2]
            phone = data[3]
            work_experience = int(data[4])
            department = data[5]
            group_id = int(data[6])
            return cls(teacher_id, name, surname, patronymic, phone, work_experience, department, group_id)



    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        teacher_id = data["teacher_id"]
        name = data["name"]
        surname = data["surname"]
        patronymic = data["patronymic"]
        phone = data["phone"]
        work_experience = data["work_experience"]
        department = data["department"]
        group_id = data["group_id"]
        return cls(teacher_id, name, surname, patronymic, phone, work_experience, department, group_id)

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not self.val_phone(value):
            raise ValueError("Ошибка ввода телефона")
        self.__phone = value
    @property
    def work_experience(self):
        return self.__work_experience

    @work_experience.setter
    def work_experience(self, value):
        if not self.val_work_experience(value):
            raise ValueError("Ошибка ввода стажа")
        self.__work_experience = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        if not self.val_department(value):
            raise ValueError("Ошибка ввода отделения")
        self.__department = value

    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, value):
        if not self.val_group_id(value):
            raise ValueError("Ошибка ввода id группы")
        self.__group_id = value

    def short_output(self):  # краткий вывод класса
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}"

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}, Phone: {self.phone}, Work Experience: {self.work_experience}, Department: {self.department}, Group ID: {self.group_id}"

    def __eq__(self, other):
        if not isinstance(other, Teacher):
            return NotImplemented
        return (
            self.teacher_id == other.teacher_id
            and self.name == other.name
            and self.surname == other.surname
            and self.patronymic == other.patronymic
            and self.phone == other.phone
            and self.department == other.department
            and self.group_id == other.group_id
        )
