import json
import re

import yaml
from abc import ABC, abstractmethod
import psycopg2
from config import host, dbname, user, password, port
from tkinter import *
from tkinter import ttk

import tkinter as tk


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

#класс преподавателей

class Teacher(ShortTeacher):
    def __init__(self, teacher_id, name, surname, patronymic, phone, work_experience, department, group_id):
        super().__init__(teacher_id, name, surname, patronymic)
        self.__phone = phone
        self.__work_experience = work_experience
        self.__department = department
        self.__group_id = group_id

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

class TeacherRepBase(ABC):

    @abstractmethod
    def add_teacher_to_file(self, teacher):
        pass

    @abstractmethod
    def get_teacher_by_id(self, teacher_id):
        pass

    @abstractmethod
    def sort_by_work_experience(self):
        pass

    @abstractmethod
    def add_teacher(self, teacher):
        pass

    @abstractmethod
    def update_teacher_by_id(self, teacher_id, t):
        pass

    @abstractmethod
    def delet(self, teacher_id):
        pass

    @abstractmethod
    def get_count(self):
        pass

    @abstractmethod
    def get_k_n_short_list(self, k, n):
        pass

class Strategy(ABC):
    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def write_all(self, data):
        pass

class TeacherRep(TeacherRepBase):
    def __init__(self, strategy: Strategy):
        self.strategy = strategy
        self.teachers = self.strategy.read_all()

    def add_teacher_to_file(self, teacher):
        self.teachers.append(teacher)
        self.strategy.write_all(self.teachers)

    def get_teacher_by_id(self, teacher_id):
        for teacher in self.teachers:
            if teacher["teacher_id"] == teacher_id:
                return teacher
        return "Такого учителя нет"

    def sort_by_work_experience(self):
        self.teachers.sort(key=lambda x: x["work_experience"])

    def is_phone_unique(self, phone):
        for teacher in self.teachers:
            if teacher.get("phone") == phone:
                return False
        return True

    def add_teacher(self, teacher):
        if not self.is_phone_unique(teacher.get("phone")):
            raise ValueError("Учитель с таким номером уже существует.")
        if not self.teachers:
            teacher["teacher_id"] = 1
        else:
            max_id = max(t["teacher_id"] for t in self.teachers)
            teacher["teacher_id"] = max_id + 1
        self.teachers.append(teacher)

    def update_teacher_by_id(self, teacher_id, t):
        for i, teacher in enumerate(self.teachers):
            if teacher["teacher_id"] == teacher_id:
                t["teacher_id"] = teacher_id
                self.teachers[i].update(t)

    def delet(self, teacher_id):
        for index, teacher in enumerate(self.teachers):
            if teacher["teacher_id"] == teacher_id:
                del self.teachers[index]
                break

    def get_count(self):
        return len(self.teachers)

    def __str__(self):
        return f"{self.teachers}"

    def get_k_n_short_list(self, k, n):
        return self.teachers[(k - 1) * n:(k - 1) * n + n]




# Стратегия для работы с JSON
class JsonStrategy(Strategy):
    def __init__(self,file):
        self.file=file

    def read_all(self):
        try:
            with open(self.file, 'r') as f:
                content = f.read()
                if not content.strip():
                    return []
                data = json.loads(content)
                return data
        except json.JSONDecodeError as e:
            print(f"Ошибка разбора JSON: {e}")
            return []

    def write_all(self, data):
        with open(self.file, 'w') as f:
            json.dump(data, f)

# Стратегия для работы с YAML
class YamlStrategy(Strategy):
    def __init__(self,file):
        self.file=file

    def read_all(self):
        try:
            with open(self.file, 'r') as f:
                return yaml.safe_load(f) or []
        except yaml.YAMLError as e:
            print(f"Ошибка разбора YAML: {e}")
            return []

    def write_all(self, data):
        with open(self.file, 'w') as f:
            yaml.dump(data, f)

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.host = kwargs.get('host')
            cls._instance.dbname = kwargs.get('dbname')
            cls._instance.user = kwargs.get('user')
            cls._instance.password = kwargs.get('password')
            cls._instance.port = kwargs.get('port')
            cls._instance.conn = None
            cls._instance.cursor = None
        return cls._instance

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.dbname,
            user=self.user,
            password=self.password,
            port=self.port
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()



class Teacher_rep_DB:
    def __init__(self, db: Database):
        self.db = db

    def get_teacher_by_id(self, teacher_id):
        self.db.cursor.execute("SELECT * FROM teachers WHERE teacher_id = %s", (teacher_id,))
        row = self.db.cursor.fetchone()
        if row:
            return Teacher(*row)
        return None

    def get_k_n_short_list(self, k, n):
        self.db.cursor.execute("SELECT teacher_id, name, surname, patronymic FROM teachers LIMIT %s OFFSET %s",
                               (n, (k - 1) * n))
        rows = self.db.cursor.fetchall()
        return [ShortTeacher(*row) for row in rows]

    def is_phone_unique(self, phone, teacher_id=None):
        self.db.cursor.execute("SELECT COUNT(*) FROM teachers WHERE phone = %s" + (f" AND teacher_id != %s" if teacher_id else ""), (phone, teacher_id) if teacher_id else (phone,))
        count = self.db.cursor.fetchone()[0]
        return count == 0

    def add_teacher(self, teacher):
        if not self.is_phone_unique(teacher.phone):
            raise ValueError("Учитель с таким номером телефона уже существует.")
        self.db.cursor.execute("INSERT INTO teachers (name, surname, patronymic, phone, work_experience, department, group_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING teacher_id",
                              (teacher.name, teacher.surname, teacher.patronymic, teacher.phone, teacher.work_experience, teacher.department, teacher.group_id))
        self.db.conn.commit()

    def update_teacher_by_id(self, teacher_id, teacher):
        if not self.is_phone_unique(teacher.phone, teacher_id):
            raise ValueError("Учитель с таким номером телефона уже существует.")
        self.db.cursor.execute("UPDATE teachers SET name = %s, surname = %s, patronymic = %s, phone = %s, work_experience = %s, department = %s, group_id = %s WHERE teacher_id = %s",
                              (teacher.name, teacher.surname, teacher.patronymic, teacher.phone, teacher.work_experience, teacher.department, teacher.group_id, teacher_id))
        self.db.conn.commit()

    def delet(self, teacher_id):
        self.db.cursor.execute("DELETE FROM teachers WHERE teacher_id = %s", (teacher_id,))
        self.db.conn.commit()

    def get_count(self):
        self.db.cursor.execute("SELECT COUNT(*) FROM teachers")
        return self.db.cursor.fetchone()[0]

    def __str__(self):
        self.db.cursor.execute("SELECT * FROM teachers")
        rows = self.db.cursor.fetchall()
        return "\n".join(str(Teacher(*row)) for row in rows)

    def teachers(self):
        self.db.cursor.execute("SELECT * FROM teachers")
        rows = self.db.cursor.fetchall()
        return [Teacher(*row) for row in rows]

    def create_table(self):
        self.db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                teacher_id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                surname VARCHAR(50) NOT NULL,
                patronymic VARCHAR(50) NOT NULL,
                phone VARCHAR(20) NOT NULL UNIQUE,
                work_experience INTEGER NOT NULL,
                department VARCHAR(50) NOT NULL,
                group_id INTEGER NOT NULL
            );
        """)
        self.db.conn.commit()


class Adapter(TeacherRepBase):
    def __init__(self, db_worker: Teacher_rep_DB):
        self.worker=db_worker

    def __str__(self):
        return str(self.worker)

    def add_teacher_to_file(self, teacher):
        pass # не используется в данном случае

    def get_teacher_by_id(self, teacher_id):
        teacher = self.worker.get_teacher_by_id(teacher_id)
        if teacher:
            return teacher.ser_obj()
        return "Такого учителя нет"

    def sort_by_work_experience(self):
        pass  # не используется в данном случае

    def add_teacher(self, teacher):
        self.worker.add_teacher(teacher)

    def update_teacher_by_id(self, teacher_id, t):
        self.worker.update_teacher_by_id(teacher_id, t)

    def delet(self, teacher_id):
        self.worker.delet(teacher_id)
    def teachers(self):
        return self.worker.teachers()

    def get_count(self):
        return self.worker.get_count()

    def get_k_n_short_list(self, k, n):
        return [teacher.ser_obj() for teacher in self.worker.get_k_n_short_list(k, n)]
    def read_all(self):
        pass# не используется в данном случае

    def write_all(self):
        pass# не используется в данном случае

def filter_by_id(teacher):
    return teacher.teacher_id<=10

def sort_by_surname(teacher):
    return teacher.surname

class FilterDecorator_DB:
    def __init__(self, teachers: Teacher_rep_DB, filter1):
        self.teachers = teachers
        self.filter = filter1

    def get_k_n_short_list(self, k, n):
        all_t = self.teachers.get_k_n_short_list(k, n)
        filtered_teachers = [ShortTeacher(teacher.teacher_id, teacher.name, teacher.surname, teacher.patronymic)
                             for teacher in all_t if self.filter(teacher)]
        return filtered_teachers

    def get_count(self):
        all_t = self.teachers.teachers()
        s = 0
        for teacher in all_t:
            if self.filter(teacher):
                s += 1
        return s


class SortDecorator_DB:
    def __init__(self, teachers:Teacher_rep_DB, sort_key):
        self.teachers = teachers
        self.sort_key = sort_key

    def get_k_n_short_list(self, k, n):
        all_teachers = self.teachers.get_k_n_short_list(k, n)
        sorted_teachers = sorted(all_teachers, key=self.sort_key)
        return sorted_teachers

    def get_count(self):
        return self.teachers.get_count()

class FilterDecorator_file:
    def __init__(self, repository: TeacherRep, filter1):
        self.repository = repository
        self.filter = filter1

    def get_k_n_short_list(self, k, n):
        all_t=self.repository.get_k_n_short_list(k,n)
        filtered_teachers = [ShortTeacher(*teacher) for teacher in all_t if self.filter(teacher)]
        return filtered_teachers

    def get_count(self):
        all_t=self.repository.teachers()
        s=0
        for teacher in all_t:
            if self.filter(teacher):
                s=s+1
        return s



class SortDecorator_file:
    def __init__(self, repository: TeacherRep, sort_key):
        self.repository = repository
        self.sort_key = sort_key

    def get_k_n_short_list(self, k, n):
        all_teachers = self.repository.get_k_n_short_list(k, n)
        sorted_teachers = sorted(all_teachers, key=self.sort_key)
        return sorted_teachers

    def get_count(self):
        return self.repository.get_count()

class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer) -> None:
        self.observers.append(observer)
        print("наблюдатель добавлен")
    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)
            print("уведомление получил!")

class TeacherController(Subject):
    def __init__(self, repository):
        super().__init__()
        self.repository = repository

        self.view = TeacherView(self)
        self.attach(self.view)

        self.view.window.mainloop()
    def refresh_teachers(self):
        try:
            teachers = self.repository.teachers()
            self.notify(teachers)
        except Exception as e:
            print(f"Ошибка при обновлении списка преподавателей: {e}")

    def add_teacher(self, teacher):
        try:
            self.repository.add_teacher(teacher)
            self.notify(self.repository.teachers())
        except Exception as e:
            print(f"Ошибка при добавлении преподавателя: {e}")

    def update_teacher(self, teacher_id, teacher_data):
        try:
            self.repository.update_teacher_by_id(teacher_id, teacher_data)
            self.notify(self.repository.teachers())
        except Exception as e:
            print(f"Ошибка при обновлении преподавателя: {e}")

    def delete_teacher(self, teacher_id):
        try:
            self.repository.delet(teacher_id)
            self.notify(self.repository.teachers())
        except Exception as e:
            print(f"Ошибка при удалении преподавателя: {e}")

class TeacherView(Observer):
    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.window.title("Управление Преподавателями")
        self.window.geometry("800x400")

        # Создание таблицы
        self.tree = ttk.Treeview(self.window, columns=("ID", "Имя", "Фамилия", "Отчество", "Телефон", "Стаж", "Кафедра", "ID Группы"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Имя", text="Имя")
        self.tree.heading("Фамилия", text="Фамилия")
        self.tree.heading("Отчество", text="Отчество")
        self.tree.heading("Телефон", text="Телефон")
        self.tree.heading("Стаж", text="Стаж")
        self.tree.heading("Кафедра", text="Кафедра")
        self.tree.heading("ID Группы", text="ID Группы")
        self.tree.pack(expand=True)

        self.refresh_button = Button(self.window, text="Обновить", command=self.refresh_teachers)
        self.refresh_button.pack()

        self.add_button = Button(self.window, text="Добавить учителя", command=self.open_add_teacher)
        self.add_button.pack()


    def open_add_teacher(self):
        AddTeacherController(self.controller.repository,self.controller)

    def update(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for teacher in data:
            self.tree.insert("", END, values=(teacher.teacher_id, teacher.name, teacher.surname, teacher.patronymic, teacher.phone, teacher.work_experience, teacher.department, teacher.group_id))

    def refresh_teachers(self):
        self.controller.refresh_teachers()  # Вызываем метод контроллера для обновления данных
class AddTeacherController:
    def __init__(self, repository, main_controller):
        self.repository = repository
        self.view = AddTeacherView(self)
        self.main_controller=main_controller
    def add_teacher(self, teacher):
        try:
            self.repository.add_teacher(teacher)
            print("Преподаватель добавлен успешно.")
            self.notify()
        except Exception as e:
            print(f"Ошибка при добавлении преподавателя: {e}")

    def notify(self):
        self.main_controller.refresh_teachers()
class AddTeacherView:
    def __init__(self, controller):
        self.controller = controller
        self.window = Toplevel()
        self.window.title("Добавить Преподавателя")
        self.window.geometry("400x300")

        self.name_label = Label(self.window, text="Имя:")
        self.name_label.pack()
        self.name_entry = Entry(self.window)
        self.name_entry.pack()

        self.surname_label = Label(self.window, text="Фамилия:")
        self.surname_label.pack()
        self.surname_entry = Entry(self.window)
        self.surname_entry.pack()

        self.patronymic_label = Label(self.window, text="Отчество:")
        self.patronymic_label.pack()
        self.patronymic_entry = Entry(self.window)
        self.patronymic_entry.pack()

        self.phone_label = Label(self.window, text="Телефон:")
        self.phone_label.pack()
        self.phone_entry = Entry(self.window)
        self.phone_entry.pack()

        self.work_experience_label = Label(self.window, text="Стаж:")
        self.work_experience_label.pack()
        self.work_experience_entry = Entry(self.window)
        self.work_experience_entry.pack()

        self.department_label = Label(self.window, text="Кафедра:")
        self.department_label.pack()
        self.department_entry = Entry(self.window)
        self.department_entry.pack()

        self.group_id_label = Label(self.window, text="ID Группы:")
        self.group_id_label.pack()
        self.group_id_entry = Entry(self.window)
        self.group_id_entry.pack()

        self.add_button = Button(self.window, text="Добавить", command=self.add_teacher)
        self.add_button.pack()

        self.cancel_button = Button(self.window, text="Отмена", command=self.window.destroy)
        self.cancel_button.pack()

    def add_teacher(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        patronymic = self.patronymic_entry.get()
        phone = self.phone_entry.get()
        work_experience = self.work_experience_entry.get()
        department = self.department_entry.get()
        group_id = self.group_id_entry.get()
        try:
            work_experience = int(work_experience)
            group_id = int(group_id)
            new_teacher = Teacher(
                teacher_id=1,
                name=name,
                surname=surname,
                patronymic=patronymic,
                phone=phone,
                work_experience=work_experience,
                department=department,
                group_id=group_id
            )
            self.controller.add_teacher(new_teacher)
            self.window.destroy()
        except ValueError as e:
            print(f"Ошибка: {e}")



'''
teacher = Teacher(1, "John", "Doe", "Junior", "89949889112", 5, "Math", 101)
print(teacher.name)
teacher2=teacher

file_json=JsonStrategy("Teachers.json")
teacher2.name = "Jane"
rep_json=TeacherRep(file_json)


print(teacher2)
print(teacher==teacher2)
print("------------------------------------------------------------------------------------")
print("jsons")

with open("example.json", "r") as f:
    data = f.read()
    teacher = Teacher.from_json(data)
    print(teacher)#полный вывод объекта
    print(teacher.short_output())# краткий вывод объекта
    short=ShortTeacher(1, "John", "Doe", "Junior")
    print(short)

strteacher="gggg bbbb hhh 89949885112 5 En 222"
strteacher=Teacher.from_string(strteacher)

rep_json.add_teacher(strteacher.ser_obj())
print(rep_json.get_teacher_by_id(5))
rep_json.sort_by_work_experience()
print(rep_json)
teacher2.name = "hhtvyhr"
teacher2.group_id=1
#rep_json.add_teacher(teacher2.ser_obj()) - выдаст ошибку телефона
teacher2.phone="89949889114"
rep_json.add_teacher(teacher2.ser_obj())
print(rep_json)
rep_json.update_teacher_by_id(3,teacher.ser_obj())
print(rep_json)
print(rep_json.get_k_n_short_list(2,1))
rep_json.delet(1)
print(rep_json)
print(rep_json.get_count())
print("------------------------------------------------------------------------------------")
print("yamls")

rep_yaml = TeacherRep(YamlStrategy("teachers.yaml"))
print(rep_yaml.get_teacher_by_id(5))

print()
print("------------------------------------------------------------------------------------")
print("база данных")
db = Database(host=host, dbname=dbname, user=user, password=password, port=port)
db.connect()

db_worker= Teacher_rep_DB(db)
db_worker.create_table()
#db_worker.add_teacher(teacher)
adapter = Adapter(db_worker)
print(adapter)
print(adapter.get_teacher_by_id(1))

print(adapter.get_k_n_short_list(1,2))
filtered_rep = FilterDecorator_DB(db_worker, filter_by_id)
sorted_rep = SortDecorator_DB(db_worker, sort_by_surname)
print(filtered_rep.get_count())

filtered_count = sorted_rep.get_k_n_short_list(1,1)
for teacher in filtered_count:
    print(teacher)
'''


if __name__ == "__main__":
    db = Database(host=host, dbname=dbname, user=user, password=password, port=port)
    db.connect()

    db_worker = Teacher_rep_DB(db)
    db_worker.create_table()
    adapter = Adapter(db_worker)

    controller = TeacherController(adapter) 
    db.close()




