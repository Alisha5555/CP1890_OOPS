import sqlite3
from contextlib import closing

from A3Q5_Class import Sales
from A3Q5_Class import Region
from A3Q5_Class import ImportedFiles

conn = None

def connect():
    global conn
    conn= sqlite3.connect("A3Q5.sqlite")
    conn.row_factory= sqlite3.row

def close():
    if conn:
        conn.close()

def addRegion(row):
    return Region(row["Code"], row["Name"])

def makeSale(row):
    return Sales(row["SalesID"], row["salesAmount"], row["salesDate"], addRegion(row))