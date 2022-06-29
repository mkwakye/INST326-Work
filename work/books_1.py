import sqlite3
import pandas
import csv

"""
Driver/Navigator: Michael Kwakye
Emails: mkwakye99@gmail.com
Assignment: Exercise 10
Date: 4_21_21

"""

#BOOK.CSV
conn = sqlite3.connect('kwakye.sqlite')
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS books''')
cq = '''CREATE TABLE books (
        id INTEGER, title TEXT, author TEXT, date INTEGER
        )'''
        
cursor.execute(cq)

data_file = open('books.csv', encoding="utf8")
data = csv.reader(data_file)

imq = '''INSERT INTO books VALUES (?,?,?,?)'''
cursor.executemany(imq, data)

#TEST CODE TO PRINT ALL OF THE "TITLES" OF BOOKS
sq = '''SELECT title FROM books'''
books = cursor.execute(sq).fetchall()
print(books)
print("--------------------------")

conn.commit()
conn.close()


#ENERGY.CSV
conn = sqlite3.connect('kwakye.sqlite')
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS production''')
eq = '''CREATE TABLE production (
        yr INTEGER, st TEXT, source TEXT, mwh INTEGER
        )'''
        
cursor.execute(eq)

data_file_two = open('energy.csv', encoding="utf8")
data_two = csv.reader(data_file_two)

emq = '''INSERT INTO production VALUES (?,?,?,?)'''
cursor.executemany(emq, data_two)

#MAX WIND
esq = '''SELECT st, source, MAX(mwh) FROM production WHERE source = "Wind"'''
energy = cursor.execute(esq).fetchall()
print(energy)
print("--------------------------")

#MAX SOLAR
esq2 = '''SELECT st, source, MAX(mwh) FROM production WHERE source = "Solar Thermal and Photovoltaic"'''
energy_2 = cursor.execute(esq2).fetchall()
print(energy_2)
print("--------------------------")

#TOTAL BY YEAR FOR WIND
esq3 = '''SELECT yr, source, SUM(mwh) AS "total" FROM production WHERE source = "Wind" GROUP BY yr;'''
energy_3 = cursor.execute(esq3).fetchall()
print(energy_3)
print("--------------------------")

#TOTAL BY YEAR FOR SOLAR
esq4 = '''SELECT yr, source, SUM(mwh) AS "total" FROM production WHERE source = "Solar Thermal and Photovoltaic" GROUP BY yr;'''
energy_4 = cursor.execute(esq4).fetchall()
print(energy_4)

conn.commit()
conn.close()
