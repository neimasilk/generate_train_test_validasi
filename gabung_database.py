import sqlite3
from reset_db import ResetDb

sql_create_id_zhcn_table = """ CREATE TABLE IF NOT EXISTS "id_zhcn" (
        `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        `text_id`	TEXT,
        `text_zhcn`	TEXT,
        `text_en_id`	TEXT,
        `text_en_zhcn`	TEXT,
        `tok_id`	TEXT,
        `tok_zhcn`	TEXT,
        `tok_en_id`	TEXT,
        `tok_en_zhcn`	TEXT
    ); """


sql_file = """attach "{}" as toMerge; BEGIN; insert into id_zhcn(text_id,text_zhcn,text_en_id) select text_id,text_zhcn,text_en_id  from toMerge.id_zhcn; COMMIT; detach database toMerge;"""

def gabung_database(file_gabungan, *args):
    try:
        rsdb = ResetDb(file_gabungan)
        rsdb.create_id_zhcn()
        db_connection = sqlite3.connect(file_gabungan)
        db_cur = db_connection.cursor()
        for arg in args:
            # print(arg)
            # print(sql_file.format(arg))
            print(arg)
            db_cur.executescript(sql_file.format(arg))

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    gabung_database('gabungan.db','indonesia_sentences_1000000.db','mandarin_sentences_1000000.db','casict.db')