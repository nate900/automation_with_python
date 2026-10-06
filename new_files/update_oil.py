# this program updates a row in the changes.db sqlite database if a user put in incorrect information
from pathlib import Path
import sqlite3
import sys

cwd = Path.cwd()
# make sure the database exists
if not (cwd / 'oil_changes/changes.db').is_file():
    print('cannot make changes to a database that does not exists')
    exit(0)

# get command line arguments
choices = ['date','cost','oil','filter','car']
rowid = 0
choice = ''
data = None
try:
    # get the row to update
    if len(sys.argv) > 1:
        rowid,choice = sys.argv[1:]
        actual_choice = False
        for item in choices:
            if item.casefold() == choice.casefold():
                choice = item
                actual_choice = True
        if not actual_choice:
            print('Enter an actual column name')
            exit(1)
        else:
            print(f'enter the information you would like to update row {rowid} and column "{choice}" with:')
            data = input()
            if choice == choices[1]:
                data = int(data) # user is changing the cost of an entry
    else:
        print('Please input the rowid followed by what you want to update. date, cost, oil, filter, or car')
        exit(1)
except ValueError as e:
    print('you need to input the rowid followed by what column you want to update')

update_stmt = f'update oil_changes set {choice} = "{data}" where rowid = {rowid}'
# get a connection to the database
try:
    db_conn = sqlite3.connect(cwd / 'oil_changes/changes.db', isolation_level=None)
    updt_row = db_conn.execute(f'select rowid, * from oil_changes where rowid = {rowid}').fetchall()
    if len(updt_row) == 0:
        print('this row does not exist')
        exit(0)
    print(f'before update {updt_row}')
    db_conn.execute(update_stmt)
    updt_row = db_conn.execute(f'select rowid, * from oil_changes where rowid = {rowid}').fetchall()
    print(f'after update {updt_row}')
except Exception as e:
    print(e)
finally:
    db_conn.close()