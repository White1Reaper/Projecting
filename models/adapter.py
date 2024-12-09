from models.teacher_rep_base import TeacherRepBase
from models.teacher_rep_db import Teacher_rep_DB
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
            return teacher
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