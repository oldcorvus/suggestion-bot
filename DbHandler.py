import sqlite3


class DBHelper:

    def __init__(self, dbname="db.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def connect(self, dbname="db.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS items (Name text , Genre text,Type text,action text,star INTEGER DEFAULT '0', id INTEGER NOT NULL PRIMARY KEY UNIQUE ,Cint INTEGER DEFAULT '0',count INTEGER DEFAULT '0' )"
        self.conn.execute(stmt)
        stmt = "CREATE TABLE IF NOT EXISTS games (Name text , Genre text,Platform text,star INTEGER DEFAULT '0', id INTEGER NOT NULL PRIMARY KEY UNIQUE ,Cint INTEGER DEFAULT '0',count INTEGER DEFAULT '0' )"
        self.conn.execute(stmt)
        self.conn.commit()

    def edit(self, id_item, name_item):
        stmt = "UPDATE items SET Name=(?) WHERE id=(?)"
        args = (name_item, id_item)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def add_item(self, name, genre, type_item, action):
        args = (name, genre, type_item, action)
        self.conn.execute('INSERT INTO items (Name, Genre,Type , action)  VALUES (?,?,?,?)', args)
        self.conn.commit()
        stmt = "SELECT * FROM items WHERE  Name =(?)"
        args = (name,)
        return [x for x in self.conn.execute(stmt, args)]

    def add_game(self, name, genre, platform):
        args = (name, genre, platform)
        self.conn.execute('INSERT INTO games (Name, Genre,platform)  VALUES (?,?,?)', args)
        self.conn.commit()
        stmt = "SELECT * FROM games WHERE  Name =(?)"
        args = (name,)
        return [x for x in self.conn.execute(stmt, args)]

    def delete_item(self, id_item):
        stmt = "DELETE FROM items WHERE id =(?)"
        args = (id_item,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def star(self, id_items, stars):
        args = (id_items,)
        star = self.conn.execute('SELECT star FROM items WHERE id = (?)', args).fetchall()
        count = self.conn.execute('SELECT count FROM items WHERE id = (?)', args).fetchall()
        count_temp = 0
        star_temp = 0
        for x in count:
            count_temp = x[0]
        for x in star:
            star_temp = x[0]
        avg = ((count_temp * star_temp) + stars) / (count_temp + 1)
        args = (avg, id_items)
        stmt = "UPDATE items SET star = (?) WHERE id = (?)"
        self.conn.execute(stmt, args)
        self.conn.commit()
        args = (count_temp + 1, id_items)
        stmt = "UPDATE items SET count = (?) WHERE id = (?)"
        self.conn.execute(stmt, args)
        self.conn.commit()

    def star_game(self, id_item, stars):
        args = (id_item,)
        item = self.conn.execute('SELECT star FROM games WHERE id = (?)', args).fetchall()
        count = self.conn.execute('SELECT count FROM games WHERE id = (?)', args).fetchall()
        count_temp = 0
        star_temp = 0
        for x in count:
            count_temp = x[0]
        for x in item:
            star_temp = x[0]
        avg = ((count_temp * star_temp) + stars) / (count_temp + 1)
        args = (avg, id_item)
        stmt = "UPDATE games SET star = (?) WHERE id = (?)"
        self.conn.execute(stmt, args)
        self.conn.commit()
        args = (count_temp + 1, id_item)
        stmt = "UPDATE games SET count = (?) WHERE id = (?)"
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self, genre, type_item, action="suggest something"):
        stmt = "SELECT * FROM items WHERE Genre=(?) AND Type=(?) AND action=(?) AND Cint=1"
        args = (genre, type_item, action)
        return [x for x in self.conn.execute(stmt, args)]

    def get_games(self, genre, platform):
        stmt = "SELECT * FROM games WHERE Genre=(?) AND platform=(?) AND Cint=1"
        args = (genre, platform)
        return [x for x in self.conn.execute(stmt, args)]

    def get_all_items(self, type_item):
        stmt = "SELECT * FROM items WHERE  Type=(?) AND Cint=1"
        args = (type_item,)
        return [x for x in self.conn.execute(stmt, args)]

    def confirm(self, id_item):
        stmt = "UPDATE items SET Cint=1 WHERE id = (?)"
        args = (id_item,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def confirm_game(self, id_item):
        stmt = "UPDATE games SET Cint=1 WHERE id = (?)"
        args = (id_item,)
        self.conn.execute(stmt, args)
        self.conn.commit()
