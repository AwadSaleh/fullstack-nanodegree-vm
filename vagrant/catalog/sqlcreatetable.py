import sqlite3
conn = sqlite3.connect('onlinstore.db')

c=conn.cursor()
c.execute('''
CREAT TABLE store
(id INTEGER PRIMARY KEY ASC,name varchar(250) NOT NULL)
''')
c.execute('''
CREAT TABLE store_item
(id INTEGER PRIMARY KEY ASC,name varchar(250),price varchar(250),
description varchar(250) NOT NULL,store_id INTEGER NOT NULL,
FOREIGN KEY (store_id) REFERENCES store(id))
''')

conn.commit()
conn.close()

