try:
    import psycopg2
except Exception as e:
    print(f"Lib not installed: %s" % e)

class DBConnector:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except Exception as e:
            raise ConnectionError(f"Connection database error: {str(e)}")

    def disconnect(self):
        if self.conn:
            self.conn.close()
