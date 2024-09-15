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

# инкапсуляция полей с помощью геттеров

    @property
    def teacher_id(self):
        return self.__teacher_id

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def phone(self):
        return self.__phone

    @property
    def work_experience(self):
        return self.__work_experience

    @property
    def department(self):
        return self.__department

    @property
    def group_id(self):
        return self.__group_id

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}, Phone: {self.phone}, Work Experience: {self.work_experience}, Department: {self.department}, Group ID: {self.group_id}"
teacher = Teacher(1, "John", "Doe", "Junior", "123-456-7890", 5, "Math", 101)
print(teacher.name)
print(teacher.teacher_id)  