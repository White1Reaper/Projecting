import psycopg2

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.host = kwargs.get('host')
            cls._instance.dbname = kwargs.get('dbname')
            cls._instance.user = kwargs.get('user')
            cls._instance.password = kwargs.get('password')
            cls._instance.port = kwargs.get('port')
            cls._instance.conn = None
            cls._instance.cursor = None
        return cls._instance

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.dbname,
            user=self.user,
            password=self.password,
            port=self.port
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()
