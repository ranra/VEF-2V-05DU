import sqlite3

# búum til gagnagrunn ef hann er ekki til og db tengingu
conn = sqlite3.connect('database.db')
print("Opened database successfully")

# búum til töflu í gagnagrunni
conn.execute("""CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)""")
print("Table created successfully")
conn.close()

# Til að búa til gagnagrunn í Pycharm;  run og svo velja database þá verður til ,,local" gagnagrunnur með .db endingu.
