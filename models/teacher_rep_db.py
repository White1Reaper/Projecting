from  models.Database import Database
from models.teacher import Teacher
from models.short_teacher import ShortTeacher

class Teacher_rep_DB:
    def __init__(self, db: Database):
        self.db = db

    def get_teacher_by_id(self, teacher_id):
        self.db.cursor.execute("SELECT * FROM teachers WHERE teacher_id = %s", (teacher_id,))
        row = self.db.cursor.fetchone()
        if row:
            return Teacher(*row)
        return None

    def get_k_n_short_list(self, k, n):
        self.db.cursor.execute("SELECT teacher_id, name, surname, patronymic FROM teachers LIMIT %s OFFSET %s",
                               (n, (k - 1) * n))
        rows = self.db.cursor.fetchall()
        return [ShortTeacher(*row) for row in rows]

    def is_phone_unique(self, phone, teacher_id=None):
        self.db.cursor.execute("SELECT COUNT(*) FROM teachers WHERE phone = %s" + (f" AND teacher_id != %s" if teacher_id else ""), (phone, teacher_id) if teacher_id else (phone,))
        count = self.db.cursor.fetchone()[0]
        return count == 0

    def add_teacher(self, teacher):
        if not self.is_phone_unique(teacher.phone):
            raise ValueError("Учитель с таким номером телефона уже существует.")
        self.db.cursor.execute("INSERT INTO teachers (name, surname, patronymic, phone, work_experience, department, group_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING teacher_id",
                              (teacher.name, teacher.surname, teacher.patronymic, teacher.phone, teacher.work_experience, teacher.department, teacher.group_id))
        self.db.conn.commit()

    def update_teacher_by_id(self, teacher_id, teacher):
        if not self.is_phone_unique(teacher.phone, teacher_id):
            raise ValueError("Учитель с таким номером телефона уже существует.")
        self.db.cursor.execute("UPDATE teachers SET name = %s, surname = %s, patronymic = %s, phone = %s, work_experience = %s, department = %s, group_id = %s WHERE teacher_id = %s",
                              (teacher.name, teacher.surname, teacher.patronymic, teacher.phone, teacher.work_experience, teacher.department, teacher.group_id, teacher_id))
        self.db.conn.commit()

    def delet(self, teacher_id):
        self.db.cursor.execute("DELETE FROM teachers WHERE teacher_id = %s", (teacher_id,))
        self.db.conn.commit()

    def get_count(self):
        self.db.cursor.execute("SELECT COUNT(*) FROM teachers")
        return self.db.cursor.fetchone()[0]

    def __str__(self):
        self.db.cursor.execute("SELECT * FROM teachers")
        rows = self.db.cursor.fetchall()
        return "\n".join(str(Teacher(*row)) for row in rows)

    def teachers(self):
        self.db.cursor.execute("SELECT * FROM teachers")
        rows = self.db.cursor.fetchall()
        return [Teacher(*row) for row in rows]

    def create_table(self):
        self.db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                teacher_id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                surname VARCHAR(50) NOT NULL,
                patronymic VARCHAR(50) NOT NULL,
                phone VARCHAR(20) NOT NULL UNIQUE,
                work_experience INTEGER NOT NULL,
                department VARCHAR(50) NOT NULL,
                group_id INTEGER NOT NULL
            );
        """)
        self.db.conn.commit()

