import mysql.connector
from mysql.connector import errorcode, pooling

def_dbconf = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'database': 'default_db'
}

class DatabaseConnection:
    def __init__(self, db_config = def_dbconf):
        self.db_config = db_config
        self.pool = None

    def init_pool(self):
        try:
            self.pool = pooling.MySQLConnectionPool(
                pool_name = self.db_config['database'],
                pool_size = 10,
                **self.db_config
            )

            print('pool initialized: {}'.format(self.db_config['database']))

            # setelah connect database, jalanin query USE {nama database}
            cnx = self.pool.get_connection()
            cursor = cnx.cursor()
            cursor.execute('USE {}'.format(self.db_config['database']))
            cursor.close()
            cnx.close()

            # self.table_check()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            quit()

    def get_connection(self):
        if (type(self.pool) == type(None)):
            self.init_pool()
        return self.pool.get_connection()
    