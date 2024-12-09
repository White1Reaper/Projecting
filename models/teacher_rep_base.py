from abc import ABC, abstractmethod

class TeacherRepBase(ABC):
    @abstractmethod
    def add_teacher_to_file(self, teacher):
        pass

    @abstractmethod
    def get_teacher_by_id(self, teacher_id):
        pass

    @abstractmethod
    def sort_by_work_experience(self):
        pass

    @abstractmethod
    def add_teacher(self, teacher):
        pass

    @abstractmethod
    def update_teacher_by_id(self, teacher_id, t):
        pass

    @abstractmethod
    def delet(self, teacher_id):
        pass

    @abstractmethod
    def get_count(self):
        pass

    @abstractmethod
    def get_k_n_short_list(self, k, n):
        pass
