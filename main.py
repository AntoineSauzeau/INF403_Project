import sqlite3

from db import create_database

con = sqlite3.connect('database.db')
cur = con.cursor()

create_database(cur)