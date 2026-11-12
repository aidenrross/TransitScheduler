import pymysql


class TransportDB:
    def __init__(self, credentials):
        h = "appstate-cs3430.mysql.database.azure.com"
        d = "random_group"
        self.connection = pymysql.connect(
            host=h, user=credentials[0], passwd=credentials[1], db=d, port=3306
        )

    def get_table(self, table):
        cursor = self.connection.cursor()
        cursor.execute("select * from '%s'", table)
        return cursor.fetchall()
