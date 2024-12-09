
from tkinter import Toplevel, Label, Entry, Button
from models.teacher import Teacher

class AddOrEditTeacherView:
    def __init__(self, controller, teacher=None):
        self.controller = controller
        self.teacher = teacher
        self.window = Toplevel()
        self.window.title("Добавить/Редактировать преподавателя")
        self.window.geometry("400x350")

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

        self.group_id_label = Label(self.window, text="ID группы:")
        self.group_id_label.pack()
        self.group_id_entry = Entry(self.window)
        self.group_id_entry.pack()

        self.save_button = Button(self.window, text="Сохранить", command=self._set_controller)
        self.save_button.pack()

        self.cancel_button = Button(self.window, text="Отмена", command=self.window.destroy)
        self.cancel_button.pack()
        if self.teacher:
            self.fields()

    def fields(self):
        self.name_entry.insert(0, self.teacher.name)
        self.surname_entry.insert(0, self.teacher.surname)
        self.patronymic_entry.insert(0, self.teacher.patronymic)
        self.phone_entry.insert(0, self.teacher.phone)
        self.work_experience_entry.insert(0, self.teacher.work_experience)
        self.department_entry.insert(0, self.teacher.department)
        self.group_id_entry.insert(0, self.teacher.group_id)

    def _set_controller(self):
        from controllers.edit_teacher_controller import EditTeacherController   #если импортировать это сразу - начинается зацикливание импортов
        if isinstance(self.controller, EditTeacherController):
            return self._edit_teacher()
        else:
            return self._add_teacher()

    def _edit_teacher(self):
        teach = self.take_teacher()
        self.controller.update_teacher(teach)
        self.window.destroy()

    def _add_teacher(self):
        teach = self.take_teacher()
        self.controller.add_teacher(teach)
        self.window.destroy()

    def take_teacher(self):
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
            view_teacher = Teacher(
                teacher_id=self.teacher.teacher_id if self.teacher else 1,
                name=name,
                surname=surname,
                patronymic=patronymic,
                phone=phone,
                work_experience=work_experience,
                department=department,
                group_id=group_id
            )
            return view_teacher
        except ValueError as e:
            print(f"Ошибка: {e}")
