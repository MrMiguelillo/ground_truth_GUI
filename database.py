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
                name = row[0]
                author = row[1]
                route = row[2]
                new_seal = seal.Seal(route, name, author)
                self.seal_list.append(new_seal)
        except RuntimeError:
            print("error: unable to fetch seals data\n")

    def insert_seal(self, name, author):
        path = "C:/Users/usuario/Desktop/new_base/" + name + ".png"
        sql = """insert into %s(nombre, autor, ruta, añadido_manual)
                 values ('%s', '%s', '%s', 1)""" % (self.table_names[0], name, author, path)

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except RuntimeError:
            self.db.rollback()
            print("unable to insert data into database\n")

    def insert_document(self, route, seal_name, coords):
        sql = """insert into %s(ruta, sello, coordenadas_x1, coordenadas_y1, coordenadas_x2, coordenadas_y2)
            values ('%s', '%s', '%s', '%s', '%s', '%s')""" % (self.table_names[1], route, seal_name,
                                                              coords[0], coords[1], coords[2], coords[3])

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except RuntimeError:
            self.db.rollback()
            print("unable to insert data into database\n")
