import phonenumbers

#класс преподавателей

class Teacher:
    def __init__(self, teacher_id, name, surname, patronymic, phone, work_experience, department, group_id):
        self.__teacher_id = teacher_id
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__phone = phone
        self.__work_experience = work_experience
        self.__department = department
        self.__group_id = group_id

    @staticmethod
    def val_teacher_id(teacher_id):
        if not isinstance(teacher_id, int) or teacher_id <= 0:
            raise ValueError("")

    @staticmethod
    def val_name(name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ошибка ввода имени")

    @staticmethod
    def val_surname(surname):
        if not isinstance(surname, str) or not surname.strip():
            raise ValueError("Ошибка ввода фамилии")

    @staticmethod
    def val_patronymic(patronymic):
        if not isinstance(patronymic, str) or not patronymic.strip():
            raise ValueError("Ошибка ввода  отчества ")

    @staticmethod
    def val_phone(phone):
        if not (phone[0]=="+" and phone[1:].isdigit() and len(phone)==12):
            raise ValueError("Ошибка ввода телефона ")

    @staticmethod
    def val_work_experience(work_experience):
        if not isinstance(work_experience, int) or work_experience < 0:
            raise ValueError("Ошибка ввода стажа")

    @staticmethod
    def val_department(department):
        if not isinstance(department, str) or not department.strip():
            raise ValueError("Ошибка ввода отделения")

    @staticmethod
    def val_group_id(group_id):
        if not isinstance(group_id, int) or group_id <= 0:
            raise ValueError("Ошибка ввода id группы")

    def __init__(self, teacher_id, name, surname, patronymic, phone, work_experience, department, group_id):
        self.val_teacher_id(teacher_id)
        self.val_name(name)
        self.val_surname(surname)
        self.val_patronymic(patronymic)
        self.val_phone(phone)
        self.val_work_experience(work_experience)
        self.val_department(department)
        self.val_group_id(group_id)

        self.__teacher_id = teacher_id
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__phone = phone
        self.__work_experience = work_experience
        self.__department = department
        self.__group_id = group_id

    # инкапсуляция полей с помощью геттеров и сеттеров

    @property
    def teacher_id(self):
        return self.__teacher_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.val_name(value)
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.val_surname(value)
        self.__surname = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        self.val_patronymic(value)
        self.__patronymic = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.val_phone(value)
        self.__phone = value

    @property
    def work_experience(self):
        return self.__work_experience

    @work_experience.setter
    def work_experience(self, value):
        self.val_work_experience(value)
        self.__work_experience = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.val_department(value)
        self.__department = value

    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, value):
        self.val_group_id(value)
        self.__group_id = value

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}, Phone: {self.phone}, Work Experience: {self.work_experience}, Department: {self.department}, Group ID: {self.group_id}"
teacher = Teacher(1, "John", "Doe", "Junior", "+79999999911", 5, "Math", 101)
print(teacher.name)

teacher.name = "Jane"
print(teacher.name)