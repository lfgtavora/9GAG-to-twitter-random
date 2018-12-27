import sqlite3

conn = sqlite3.connect('database/memes.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS memes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(200),
        link VARCHAR(100) NOT NULL UNIQUE,
        type VARCHAR(6) NOT NULL
    );
''')


def insertdb(title, link, post_type):
    cursor.execute('''
        INSERT OR IGNORE INTO memes(title, link, type) VALUES(?,?,?)''', (title, link, post_type))

    conn.commit()


# get a random post them delete from database
def getpost():
    cursor.execute('''
        SELECT * FROM memes WHERE type = 'video' ORDER BY RANDOM() LIMIT 1''')

    data = cursor.fetchall()
    id = data[0][0]
    title = data[0][1]
    link = data[0][2]
    post_type = data[0][3]

    delete_query = '''DELETE FROM memes WHERE id = ?'''

    cursor.execute(delete_query, (id,))

    conn.commit()

    return title, link, post_type
