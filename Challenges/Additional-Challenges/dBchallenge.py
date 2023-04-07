import sqlite3

rosterValues = [('Jean-Baptiste Zorg', 'Human', 122),
                ('Korben Dallas', 'Meat Popsicle', 100),
                ('Ak\'not', 'Mangalore', -5)]

conn = sqlite3.connect(":memory:")
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Roster( \
                    Name TEXT, \
                    Species TEXT, \
                    IQ INTEGER \
                    )")
    conn.commit()

    cur.executemany("INSERT INTO Roster VALUES (?, ?, ?)", rosterValues)

    conn.commit()

    cur.execute("UPDATE Roster SET Species=? WHERE Name=?", \
                ('Human', 'Korben Dallas'))

    conn.commit()

    cur.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
    for row in cur.fetchall():
        print(row)

