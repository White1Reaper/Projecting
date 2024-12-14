
from controllers.add_teacher_controller import AddTeacherController
from controllers.edit_teacher_controller import EditTeacherController
from tkinter import Tk, Button, ttk, VERTICAL, HORIZONTAL

class TeacherView:
    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.window.title("Управление Преподавателями")
        self.window.geometry("1000x400")

        # Создание фрейма для таблицы и прокрутки
        frame = ttk.Frame(self.window)
        frame.pack(expand=True, fill='both')

        # Создание таблицы
        self.tree = ttk.Treeview(frame, columns=("ID", "Имя", "Фамилия", "Отчество", "Телефон", "Стаж", "Кафедра", "ID Группы"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Имя", text="Имя")
        self.tree.heading("Фамилия", text="Фамилия")
        self.tree.heading("Отчество", text="Отчество")
        self.tree.heading("Телефон", text="Телефон")
        self.tree.heading("Стаж", text="Стаж")
        self.tree.heading("Кафедра", text="Кафедра")
        self.tree.heading("ID Группы", text="ID Группы")

        for col in self.tree["columns"]:
            self.tree.column(col, width=100)
        self.scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)

        self.scrollbar.pack(side='right', fill='y')
        self.tree.pack(expand=True, fill='both')

        self.refresh_button = Button(self.window, text="Обновить", command=self.refresh_teachers)
        self.refresh_button.pack()

        self.add_button = Button(self.window, text="Добавить учителя", command=self.open_add_teacher)
        self.add_button.pack()

        self.edit_button = Button(self.window, text="Редактировать учителя", command=self.open_edit_teacher)
        self.edit_button.pack()

        self.delete_button = Button(self.window, text="Удалить учителя", command=self.delete_teacher)
        self.delete_button.pack()

    def open_edit_teacher(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_id = selected_item[0]
            item_values = self.tree.item(item_id, 'values')
            teacher_id = item_values[0]
            teacher = self.controller.repository.get_teacher_by_id(teacher_id)
            if teacher:
                EditTeacherController(self.controller.repository, self.controller, teacher)
        else:
            print("выберите преподавателя для редактирования")

    def delete_teacher(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_id = selected_item[0]
            item_values = self.tree.item(item_id, 'values')
            teacher_id = item_values[0]
            self.controller.delete_teacher(teacher_id)
        else:
            print("выберите преподавателя для удаления")

    def open_add_teacher(self):
        AddTeacherController(self.controller.repository, self.controller)

    def update(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for teacher in data:
            self.tree.insert("", "end", values=(teacher.teacher_id, teacher.name, teacher.surname, teacher.patronymic, teacher.phone, teacher.work_experience, teacher.department, teacher.group_id))

    def refresh_teachers(self):
        self.controller.refresh_teachers()  # Вызываем метод контроллера для обновления данных
