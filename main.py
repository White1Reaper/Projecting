from config import host, dbname, user, password, port
from models.Database import Database
from controllers.teacher_controller import TeacherController
from models.adapter import Adapter
from models.teacher_rep_db import Teacher_rep_DB

class MainFact:
    def __init__(self, host, dbname, user, password, port):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port

    def conn_db(self):
        db = Database(host=self.host, dbname=self.dbname, user=self.user, password=self.password, port=self.port)
        db.connect()
        return db

    def rep(self, db):
        db_worker = Teacher_rep_DB(db)
        db_worker.create_table()
        return Adapter(db_worker)

    def create_controller(self, repository):
        return TeacherController(repository)

def main():
    fact = MainFact(host, dbname, user, password, port)
    db = fact.conn_db()
    repository = fact.rep(db)
    fact.create_controller(repository)
    db.close()

if __name__ == "__main__":
    main()
