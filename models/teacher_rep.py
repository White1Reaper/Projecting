from models.teacher_rep_base import TeacherRepBase
from strategies.strategy import Strategy

class TeacherRep(TeacherRepBase):
    def __init__(self, strategy: Strategy):
        self.strategy = strategy
        self.teachers = self.strategy.read_all()

    def add_teacher_to_file(self, teacher):
        self.teachers.append(teacher)
        self.strategy.write_all(self.teachers)

    def get_teacher_by_id(self, teacher_id):
        for teacher in self.teachers:
            if teacher["teacher_id"] == teacher_id:
                return teacher
        return "Такого учителя нет"

    def sort_by_work_experience(self):
        self.teachers.sort(key=lambda x: x["work_experience"])

    def is_phone_unique(self, phone):
        for teacher in self.teachers:
            if teacher.get("phone") == phone:
                return False
        return True

    def add_teacher(self, teacher):
        if not self.is_phone_unique(teacher.get("phone")):
            raise ValueError("Учитель с таким номером уже существует.")
        if not self.teachers:
            teacher["teacher_id"] = 1
        else:
            max_id = max(t["teacher_id"] for t in self.teachers)
            teacher["teacher_id"] = max_id + 1
        self.teachers.append(teacher)

    def update_teacher_by_id(self, teacher_id, t):
        for i, teacher in enumerate(self.teachers):
            if teacher["teacher_id"] == teacher_id:
                t["teacher_id"] = teacher_id
                self.teachers[i].update(t)

    def delet(self, teacher_id):
        for index, teacher in enumerate(self.teachers):
            if teacher["teacher_id"] == teacher_id:
                del self.teachers[index]
                break

    def get_count(self):
        return len(self.teachers)

    def __str__(self):
        return f"{self.teachers}"

    def get_k_n_short_list(self, k, n):
        return self.teachers[(k - 1) * n:(k - 1) * n + n]



