from models.teacher_rep import TeacherRep


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