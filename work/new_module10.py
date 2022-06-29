import pandas as pd
import csv
import sqlite3

# Import CSV
'''data = pd.read_csv ('books.csv')   
df = pd.DataFrame(data, columns = ['Number','Title','Author','Year'])

# Connect to SQL Server
conn = sqlite3.connect('kwakye.sqlite')
cursor = conn.cursor()

# Create Table
cursor.execute('DROP TABLE books')
cursor.execute('CREATE TABLE books (Number INT, Title TEXT, Author TEXT, Year INTEGER)')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.executemany('INSERT INTO books VALUES (?,?,?,?)'', df)
    
conn.commit()'''

conn = sqlite3.connect('kwakye.sqlite')
cursor = conn.cursor()

cursor.execute('DROP TABLE books')
cursor.execute('CREATE TABLE books (Number INT, Title TEXT, Author TEXT, Year INTEGER)')

with open('books.csv', 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    
    next(reader)
    
    for row in reader:
        cursor.execute(
        "INSERT INTO books VALUES (?, ?, ?, ?)",
        row
    )
conn.commit()