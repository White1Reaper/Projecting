class ShortTeacher:
    def __init__(self, teacher_id, name, surname, patronymic):
        self.teacher_id = teacher_id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    @staticmethod
    def val_teacher_id(teacher_id):
        return isinstance(teacher_id, int) and teacher_id > 0

    @staticmethod
    def val_name(name):
        return isinstance(name, str) and bool(name.strip())

    @staticmethod
    def val_surname(surname):
        return isinstance(surname, str) and bool(surname.strip())

    @staticmethod
    def val_patronymic(patronymic):
        return isinstance(patronymic, str) and bool(patronymic.strip())

    @property
    def teacher_id(self):
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        if self.val_teacher_id(value):
            self.__teacher_id = value
        else:
            raise ValueError("Ошибка ввода id")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if self.val_name(value):
            self.__name = value
        else:
            raise ValueError("Ошибка ввода имени")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if self.val_surname(value):
            self.__surname = value
        else:
            raise ValueError("Ошибка ввода фамилии")

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        if self.val_patronymic(value):
            self.__patronymic = value
        else:
            raise ValueError("Ошибка ввода отчества")

    def ser_obj(self):
        return {
            'teacher_id': self.teacher_id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,

        }


    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Surname: {self.surname}, Patronymic: {self.patronymic}"
