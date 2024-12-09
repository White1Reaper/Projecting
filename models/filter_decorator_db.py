from models.short_teacher import ShortTeacher
from models.teacher_rep_db import Teacher_rep_DB

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
