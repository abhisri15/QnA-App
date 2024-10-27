import sqlite3
from flask import Flask, g

def connect_db():
    sql=sqlite3.connect('F:\\IIIT Bhubaneswar\\ML\\QnA_App\\questions.db')
    sql.row_factory=sqlite3.Row  # converting tuples to dictionaries
    return sql

def get_db():
    if not hasattr(g,'sqlite3_db'):
        g.sqlite3_db=connect_db()
    return g.sqlite3_db