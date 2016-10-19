import pymysql
import seal


class Database:
    def __init__(self, db_name, user_name, passwd, tables):
        self.seal_list = []  # list of currently stored seals
        self.seals_db = pymysql.connect("localhost", user_name, passwd, tables[0])
        self.seals_cursor = self.seals_db.cursor()
        self.docs_db = pymysql.connect("localhost", user_name, passwd, tables[1])
        self.docs_cursor = self.docs_db.cursor()

        self.table_names = tables

    def load_seals(self):
        sql = "select * from %s" % self.table_names[0]

        try:
            self.seals_cursor.execute(sql)
            result = self.seals_cursor.fetchall()

            for row in result:
                name = row[0]
                author = row[1]
                route = row[2]
                new_seal = seal.Seal(route, name, author)
                self.seal_list.append(new_seal)
        except:
            print("error: unable to fetch seals data")
