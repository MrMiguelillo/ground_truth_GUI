import pymysql
import seal


class Database:
    def __init__(self, db_name, user_name, passwd, tables):
        self.seal_list = []  # list of currently stored seals
        self.db = pymysql.connect("localhost", user_name, passwd, db_name)
        self.cursor = self.db.cursor()
        self.table_names = tables

    def load_seals(self):
        sql = "select * from %s" % self.table_names[0]

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()

            for row in result:
                name = row[1]
                author = row[2]
                route = row[3]
                new_seal = seal.Seal(route, name, author)
                self.seal_list.append(new_seal)
        except:
            print("error: unable to fetch seals data")
