import sqlite3
from random import shuffle
from sqlite3.dbapi2 import Cursor

filepath = 'gabungan.db'



# select jumlah data, prosentase train dan testing (misal train 95% testing 5%)

# generate data dan simpan kedalam file :
# train.id
# test.id
#
# train.en
# test.en
#
# train.zh
# test.zh

def add_to_text_file(filename,text):
    with open(filename, 'a') as f:
        f.write("%s\n" % text)
    f.close()
# s = s.replace('\r\n', '\n')
def generate(test_persen):
    db_connection = sqlite3.connect(filepath)
    db_cur = db_connection.cursor()  # type: Cursor
    db_cur.execute(
        "select id, text_id, text_en_id, text_zhcn from id_zhcn where (text_en_id is not NULL) and (text_zhcn is not NULL) and (text_id is not NULL) order by random() ")
    textnya = db_cur.fetchall()
    train_persen = 100-test_persen
    jumlah_data = len(textnya)
    train_data = int(jumlah_data * (train_persen/100))
    testing_data = int(jumlah_data-train_data)
    test_range = list(range(jumlah_data))
    shuffle(test_range)
    test_range=test_range[:testing_data]
    train_count = 0
    count_test=0  # type: int
    test_range.sort()
    for text in textnya:
        if test_range[count_test]==train_count:
            add_to_text_file('test.id.txt', text[1].strip())
            add_to_text_file('test.en.txt', text[2].strip())
            add_to_text_file('test.zhcn.txt', text[3].strip())
            if count_test<testing_data-1:
                count_test+=1
        add_to_text_file('train.id.txt', text[1].strip())
        add_to_text_file('train.en.txt', text[2].strip())
        add_to_text_file('train.zhcn.txt', text[3].strip())
        train_count+=1

if __name__ == '__main__':
    generate(0.4)