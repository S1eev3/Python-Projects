import sqlite3

# create db and table
conn = sqlite3.connect('test2.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_file TEXT)")
    conn.commit()

conn = sqlite3.connect('test2.db')

# tuple of files
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each object in tuple to locate files with extension .txt
for f in fileList:
    if f.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # The value for each row will be one file from the tuple so (x,)
            # denotes a one element tuple for each file ending with .txt
            cur.execute("INSERT INTO tbl_txtFiles (col_file) VALUES (?)", (f,))
            print(f)
conn.close()
