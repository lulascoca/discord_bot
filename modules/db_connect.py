#!/usr/bin/python3

import MySQLdb as sql
import json

def connect_db(usr, password, database):
	db = sql.connect(host = "localhost",
					user = usr,
					passwd = password,
					db = database)
	return db
