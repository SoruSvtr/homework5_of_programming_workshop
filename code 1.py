import sqlite3
from sqlite3 import Error


def insert_data(con, cur):
    date = input('enter the date: ')
    category = input('enter the category: ')
    cost = float(input('enter the cost: '))
    description = input('enter the description: ')
    entity = (date, category, cost, description)
    cur.execute('''INSERT INTO Expenses(date, category, cost, description) VALUES(?, ?, ?, ?)''', entity)
    con.commit()
    
def view_Alldata(cur):
    cur.execute('SELECT * FROM Expenses')
    return cur.fetchall()

def update_data(con, cur):
    '''this function has the feature to update id, date, category, cost and description'''
    
    new_data_name = input('is your selection "cost"? (if yes: y\nelse:any alphaetical character)')   #new_data_name = input('what do you want to update:')
    if new_data_name == 'y' or new_data_name == 'Y': #if new_data_name == 'cost':
        id = int(input('enter the id: '))
        new_data_value = float(input('enter the new cost: '))
        cur.execute(f'UPDATE Expenses SET cost =? WHERE id =?', (new_data_value, id))
        con.commit()
    
    # elif new_data_name == 'id':
    #     id = int(input('enter the id: '))
    #     new_data_value = int(input('enter the new id: '))
    #     cur.execute(f'UPDATE Expenses SET id =? WHERE id =?', (new_data_value, id))
    #     con.commit()
        
    # elif new_data_name in ('date', 'category', 'description'):
    #     id = int(input('enter the id: '))
    #     new_data_value = input(f'enter the new {new_data_name}: ')
    #     cur.execute(f'UPDATE Expenses SET {new_data_name} =? WHERE id =?', (new_data_value, id))
    #     con.commit()
            
    else:
        print(f'back to PET\n') #print(f'{new_data_name} is not in the database')
    
def delete_data(con, cur):
    id = int(input('enter the id: '))
    cur.execute(f'DELETE FROM Expenses WHERE id =?', (id, ))
    con.commit()

try:
    con = sqlite3.connect('mydatabase.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Expenses(id integer PRIMARY KEY AUTOINCREMENT, date TEXT, category TEXT, cost REAL, description TEXT)')
    con.commit()
except Error:
    print(Error)

while True:
    try:
        command = int(input('Personal Expense Tracker\n[1]Insert Expense\n[2]view Expenses\n[3]update Expense\n[4]delete Expense\n[5]Exit\nplease choose your command: '))
        if command == 1:
            insert_data(con, cursor)
            
        elif command == 2:
            # rows = view_Alldata(con, cursor)
            # for row in rows:
            #     print(row)
            [print(rows) for rows in view_Alldata(cursor)]
            
        elif command == 3:
            update_data(con, cursor)
            
        elif command == 4:
            delete_data(con, cursor)
            
        elif command == 5:

            con.close()
            break
        
    except ValueError:
        print('Invalid command\ntry again')
