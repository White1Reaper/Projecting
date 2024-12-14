from views.add_or_edit_teacher_view import AddOrEditTeacherView

class AddTeacherController:
    def __init__(self, repository, main_controller):
        self.repository = repository
        self.view = AddOrEditTeacherView(self)
        self.main_controller = main_controller

    def add_teacher(self, teacher):
        try:
            self.repository.add_teacher(teacher)
            print("Преподаватель добавлен успешно.")
            self.notify()
        except Exception as e:
            print(f"Ошибка при добавлении преподавателя: {e}")

    def notify(self):
        self.main_controller.refresh_teachers()
