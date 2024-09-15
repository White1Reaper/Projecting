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

    # инкапсуляция полей с помощью геттеров и сеттеров

    @property
    def teacher_id(self):
        return self.__teacher_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        self.__patronymic = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def work_experience(self):
        return self.__work_experience

    @work_experience.setter
    def work_experience(self, value):
        self.__work_experience = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.__department = value

    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, value):
        self.__group_id = value

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}, Phone: {self.phone}, Work Experience: {self.work_experience}, Department: {self.department}, Group ID: {self.group_id}"

teacher = Teacher(1, "John", "Doe", "Junior", "123-456-7890", 5, "Math", 101)
print(teacher.name)

teacher.name = "Jane"
print(teacher.name)