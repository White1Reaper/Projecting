from views.add_or_edit_teacher_view import AddOrEditTeacherView

class EditTeacherController:
    def __init__(self, repository, main_controller, teacher):
        self.repository = repository
        self.main_controller = main_controller
        self.view = AddOrEditTeacherView(self, teacher)

    def update_teacher(self, teacher):
        try:
            self.repository.update_teacher_by_id(teacher.teacher_id, teacher)
            print("Преподаватель обновлен успешно.")
            self.notify()
        except Exception as e:
            print(f"Ошибка при обновлении преподавателя: {e}")

    def notify(self):
        self.main_controller.refresh_teachers()

