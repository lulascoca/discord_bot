#!/usr/bin/python3

import sys
import MySQLdb as sql
sys.path.append("../")
import modules.db_connect as db_

db = db_.connect_db("lulaz", "toor", "disc_bot")

cur = db.cursor()

def return_names():
	cur.execute("SELECT * FROM gamble;")
	a = cur.fetchall()
	b = []
	for row in a:
		b.append(row[1])
	return b

def add_user(user_name, points = 0):
	cur.execute("INSERT INTO gamble(user_name, points) VALUES(%s, %s);", (user_name, points,))
	db.commit()

def assign_points(user_name, points):
	cur.execute("UPDATE gamble SET points = %s WHERE user_name = %s;", (points, user_name,))
	db.commit()

def close_cur():
	cur.close()	
