from models.teacher_rep_db import Teacher_rep_DB


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