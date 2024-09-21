import json
import re
class ShortTeacher():
    def __init__(self, teacher_id, name, surname, patronymic):
        self.__teacher_id = self.val_teacher_id(teacher_id)
        self.__name = self.val_name(name)
        self.__surname = self.val_surname(surname)
        self.__patronymic = self.val_patronymic(patronymic)

    @staticmethod
    def val_teacher_id(teacher_id):
        if not isinstance(teacher_id, int) or teacher_id <= 0:
            raise ValueError("")
        return teacher_id

    @staticmethod
    def val_name(name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ошибка ввода имени")
        return name

    @staticmethod
    def val_surname(surname):
        if not isinstance(surname, str) or not surname.strip():
            raise ValueError("Ошибка ввода фамилии")
        return surname

    @staticmethod
    def val_patronymic(patronymic):
        if not isinstance(patronymic, str) or not patronymic.strip():
            raise ValueError("Ошибка ввода  отчества ")
        return patronymic

    @property
    def teacher_id(self):
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        self.__teacher_id=self.val_surname(value)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name=self.val_name(value)
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname=self.val_surname(value)

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        self.__patronymic=self.val_patronymic(value)

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}"

#класс преподавателей

class Teacher(ShortTeacher):
    def __init__(self, teacher_id, name, surname, patronymic, phone, work_experience, department, group_id):
        super().__init__(teacher_id,name,surname,patronymic)
        self.__phone = self.val_phone(phone)
        self.__work_experience = work_experience
        self.__department = self.val_department(department)
        self.__group_id = self.val_group_id(group_id)




    @staticmethod
    def val_phone(phone):
        if not  re.match('^(\+?7|8)\d{3}\d{3}\d{2}\d{2}$', phone):
            raise ValueError("Ошибка ввода телефона ")
        return phone

    @staticmethod
    def val_work_experience(work_experience):
        if not isinstance(work_experience, int) or work_experience < 0:
            raise ValueError("Ошибка ввода стажа")
        return work_experience

    @staticmethod
    def val_department(department):
        if not isinstance(department, str) or not department.strip():
            raise ValueError("Ошибка ввода отделения")
        return department

    @staticmethod
    def val_group_id(group_id):
        if not isinstance(group_id, int) or group_id <= 0:
            raise ValueError("Ошибка ввода id группы")
        return group_id

    @classmethod
    def from_string(cls, s):
        data = s.split(", ")
        teacher_id = int(data[0])
        name = data[1]
        surname = data[2]
        patronymic = data[3]
        phone = data[4]
        work_experience = int(data[5])
        department = data[6]
        group_id = int(data[7])
        return cls(teacher_id, name, surname, patronymic, phone, work_experience, department, group_id)

    @classmethod
    def from_json(cls, json_str):  #инициализация класса из данных в формате json
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

    @classmethod
    def from_string(cls, s):  #инициализация класса из данных в строковом типе (данные записаны через пробел)
        data = s.split(", ")
        teacher_id = int(data[0])
        name = data[1]
        surname = data[2]
        patronymic = data[3]
        phone = data[4]
        work_experience = int(data[5])
        department = data[6]
        group_id = int(data[7])
        return cls(teacher_id, name, surname, patronymic, phone, work_experience, department, group_id)
  # инкапсуляция полей с помощью геттеров и сеттеров
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, value):
                self.__phone=self.val_phone(value)

    @property
    def work_experience(self):
        return self.__work_experience

    @work_experience.setter
    def work_experience(self, value):
        self.__work_experience=self.val_work_experience(value)

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.__department=self.val_department(value)

    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, value):
        self.__group_id=self.val_group_id(value)

    def __str__(self): #полный вывод класса
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}, Phone: {self.phone}, Work Experience: {self.work_experience}, Department: {self.department}, Group ID: {self.group_id}"

    def short_output(self):  # краткий вывод класса
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}"

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

teacher = Teacher(1, "John", "Doe", "Junior", "89949889112", 5, "Math", 101)
print(teacher.name)
teacher2=teacher
teacher2.name = "Jane"
print(teacher==teacher2)
with open("example.json", "r") as f:
    data = f.read()
    teacher = Teacher.from_json(data)
    print(teacher)#полный вывод объекта
    print(teacher.short_output())# краткий вывод объекта
    short=ShortTeacher(1, "John", "Doe", "Junior")
    print(short)