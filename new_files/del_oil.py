import sqlite3
from pathlib import Path
import sys

cwd = Path.cwd()

rowid = 0

# get command line arguments
if len(sys.argv) > 1:
    rowid = sys.argv[1]
else:
    print('must enter the rowid of row you want to delete')
    exit(1)


# make sure the db exists
if (cwd / 'oil_changes/changes.db').is_file():
    try:
        db_conn = sqlite3.connect((cwd / 'oil_changes/changes.db'), isolation_level=None)
        row = db_conn.execute(f'select * from oil_changes where rowid = {rowid}').fetchall()
        print(f'you are deleting this {row} row from the DB')
        print('press 1 to continue 0 to exit')
        yes_no = int(input())
        if yes_no == 1:
            db_conn.execute(f'delete from oil_changes where rowid = {rowid}') # delete the row
            db_conn.close()
        else:
            print('row not deleted')
            exit(yes_no)
    except Exception as e:
        print(e)
else:
    print('database does not exist. Run oil_change.py')