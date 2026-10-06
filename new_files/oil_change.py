# create a program that takes the date of an oil change, the cost, oil, and filter used. Then, saves the information to a local database.

# sqlite data types
# Null
# Int
# Real
# Text
# Blob

# storing the dates in this format YYYY-MM-DD

import sys
import os
from pathlib import Path
import sqlite3

cwd = Path.cwd()
oil_changes = None

date = ''
cost = 0.0
oil = ''
filter = ''
car = ''

# get command line arguments
if len(sys.argv) > 1:
    date,cost,oil,filter,car = sys.argv[1:]
else:
    print('Please input date, cost, oil used, filter used, and car')
    exit(1)

# if oil_changes dir does not exist, then create it
if not (cwd / 'oil_changes').is_dir():
    (cwd / 'oil_changes').mkdir(exist_ok=True)
    oil_changes = (cwd / 'oil_changes')
else:
    print("oil_changes dir already exists!")
    oil_changes = (cwd / 'oil_changes')

# oil_changes dir is the dir that will store the database file
# database file is called changes.db
# test to see if db file exists
db_conn = None
if (oil_changes / 'changes.db').is_file():
    # db exists no need to reconfigure
    print('no need to create the db file')
    db_conn = sqlite3.connect((oil_changes / 'changes.db'), isolation_level=None)
else:
    db_conn = sqlite3.connect((oil_changes / 'changes.db'), isolation_level=None) # this line will create the db file
    print('db file was created')
    # add the table
    create_table = 'create table if not exists oil_changes (date text not null, cost real, oil text, filter text, car text)' # sqlite automatically creates primary key called 'rowid'
    db_conn.execute(create_table)
    # make sure table was created
    select = 'select name from sqlite_schema where type="table"'
    if len(db_conn.execute(select).fetchall()) < 1:
        print('Table was not created. Please try again later')
        db_conn.close()
        exit(1)
    else:
        print('Table was created')

try:
    # insert the provided data into the db
    insert_stmt = f'insert into oil_changes values("{date}", {cost}, "{oil}", "{filter}", "{car}")'
    db_conn.execute(insert_stmt)

    print(db_conn.execute('select * from oil_changes').fetchall())
except Exception as e:
    print(e)
    db_conn.close()
    exit(1)

db_conn.close()

