#!/usr/bin/python3

import sys
import MySQLdb as sql
sys.path.append("../")
import modules.db_connect as db_

db = db_.connect_db("lulaz", "toor", "disc_bot")

cur = db.cursor()

def add_user(user_name, points = 0):
	cur.execute("INSERT INTO gamble(user_name, points) VALUES(%s, %s);", (user_name, points,))
	db.commt()

def assign_points(user_name, points):
	cur.execute("UPDATE gamble SET points = %s WHERE user_name = '%s';", (points, user_name))

cur.close()
