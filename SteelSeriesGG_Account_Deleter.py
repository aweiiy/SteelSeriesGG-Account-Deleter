import sqlite3

print("Made by Aweiiy")
print("Aweiiy#0555")
print("\n\nDeleting all the SteelSeries GG users...")

db = sqlite3.connect(r"C:\ProgramData\SteelSeries\GG\gg-db\database.db")

cursor = db.cursor()

cursor.executescript("DELETE FROM users")
print(f"(DONE) Cleaned with success! {cursor.fetchall()}")
db.commit()
db.close()

