import sys
import MySQLdb as sql
sys.path.append("../")
import modules.db_connect as db_

db = db_.connect_db("lulaz", "toor", "disc_bot")

cur = db.cursor()

cur.execute("SELECT * FROM cats")

for row in cur:
	print(row[2])
