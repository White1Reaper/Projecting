from models.short_teacher import ShortTeacher
from models.teacher_rep import TeacherRep


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