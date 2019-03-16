#!/usr/bin/python3

import sys
import MySQLdb as sql
import random
sys.path.append("../")
import modules.db_connect as db_


db = db_.connect_db("lulaz", "toor", "disc_bot")

cur = db.cursor()

def add_user(user_name, points = 0):
	cur.execute("INSERT INTO gamble(user_name, points) VALUES(%s, %s);", (user_name, points,))
	db.commit()

def return_names():
	cur.execute("SELECT * FROM gamble;")
	a = cur.fetchall()
	b = []
	for row in a:
		b.append(row[1])
	return b

def assign_points(user_name, points):
	cur.execute("UPDATE gamble SET points = %s WHERE user_name = %s;", (points, user_name,))
	db.commit()

def return_points(user_name):
	cur.execute("SELECT * FROM gamble where user_name = %s;", (user_name,))
	a = cur.fetchall()
	curr_points = a[0][2]
	return curr_points

# coin th
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
			return("You won! You now have " + str(points) + " points.")
		else:
			current_points = a[0][2]
			points = current_points - bet_points
			cur.execute("UPDATE gamble SET points = %s WHERE user_name = %s;", (str(points), user_name,))
			db.commit()
			return("You lost! You now have " + str(points) + " points.")
	else:
		return("You don't have enough points to bet rn with that ammount try a lower one or if you don't have more points ask a mod to give you some")

def close_cur():
	cur.close()	