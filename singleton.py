import pymysql

class BotDB:
    _instance = None
    _initialized = False

    def __new__(cls, host, user, password, db_name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host, user, password, db_name):
        if not self._initialized:
            self.conn = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                charset='utf8',
                use_unicode=True,
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.conn.cursor()
            self._initialized = True

    def get_user(self, id):
        self.conn.ping()
        self.cursor.execute(
            "SELECT `user_id`, `name`, `grade`, `hobby`, `username`, `add_info`, `diapason` FROM `users1` WHERE `id`=%s",
            (id,)
        )
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()
