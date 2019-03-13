#!/usr/bin/python3

import sys
import MySQLdb as sql
import random
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

def return_points(user_name):
	cur.execute("SELECT * FROM gamble where user_name = %s;", (user_name,))
	a = cur.fetchall()
	curr_points = a[0][2]
	return curr_points

# NOT FINISHED LINE 162 bot.py
def coin_game(user_name, bet_points):
	cur.execute("SELECT * FROM gamble where user_name = %s;", (user_name,))
	a = cur.fetchall()
	curr_points = a[0][2]
	has_enough_points = curr_points >= bet_points
	if has_enough_points:
		rand_choice = random.choice([0, 1])
		if rand_choice == 1:
			current_points = a[0][2]
			points = current_points + bet_points
			cur.execute("UPDATE gamble SET points = %s WHERE user_name = %s;", (str(points), user_name,))
			db.commit()
			return points
		else:
			current_points = a[0][2]
			points = current_points - bet_points
			cur.execute("UPDATE gamble SET points = %s WHERE user_name = %s;", (str(points), user_name,))
			db.commit()
			return points
	else:
		return 0

def close_cur():
	cur.close()	

coin_game(user_name = "lulascoca", bet_points=3)