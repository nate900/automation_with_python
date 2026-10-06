# this program will select a specfic entry from the oil change database
import sys
from pathlib import Path
import sqlite3

cwd = Path.cwd()

# get command line arguments

try:
    if(cwd / 'oil_changes/changes.db').is_file():
        db_conn = sqlite3.connect((cwd / 'oil_changes/changes.db'), isolation_level=None)
        #oil_changes = db_conn.execute('select rowid, date, cost, oil, filter, car from oil_changes').fetchall()
        oil_changes = db_conn.execute('select rowid, * from oil_changes').fetchall()
        print(oil_changes)
        db_conn.close()
    else:
        print('could not connect')
except Exception as e:
    print(e)