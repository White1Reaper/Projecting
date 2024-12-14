from controllers.subject import Subject
from views.teacher_view import TeacherView
class TeacherController(Subject):
    def __init__(self, repository):
        super().__init__()
        self.repository = repository

        self.view = TeacherView(self)
        self.attach(self.view)
        self.refresh_teachers()
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
