from tkinter import *
from tkcalendar import *
import sqlite3
from PIL import ImageTk, Image
import random
from tabulate import tabulate
import tkinter.ttk as ttk
root = Tk()
root.title('EXxZAM To do list')
root.geometry('300x500')

# Databases

# Create a database or connect to one
conn = sqlite3.connect('task.db')

# Create a Cursor sends and gets results
c = conn.cursor()

# Create table

# c.execute("""CREATE TABLE tasks_user (
#         task text,
#         date text

#         )""")



def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('task.db')

    # Create a Cursor sends and gets results
    c = conn.cursor()

    # Insert into database
    c.execute('INSERT INTO tasks_user VALUES (:task_entry, :date_entry)',
              {
                  'task_entry':task_entry.get(),
                  'date_entry': date_entry.get()
              })

    # Commiting data
    conn.commit()
    # close connection
    conn.close()
    # Clear Entries
    task_entry.delete(0, END)
    date_entry.delete(0, END)
    query()

# delete record func
def delete_record():
    # Create a database or connect to one
    conn = sqlite3.connect('task.db')

    # Create a Cursor sends and gets results
    c = conn.cursor()
    try:
        c.execute('DELETE from tasks_user WHERE oid='+delete_entry.get())
    except Exception:
        label_Error = Label(root, text='Please Enter A Valid ID')
        label_Error.grid(row=10, column=0, columnspan=2)
    delete_entry.delete(0, END)
    
    # Commiting data
    conn.commit()

    # close connection
    conn.close()
    query()


# Qeury Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('task.db')

    # Create a Cursor sends and gets results
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM tasks_user ")
    records = c.fetchall()
    print_records= ''
    treetime = ttk.Treeview(root)
    treetime.grid(row=7, column=0, columnspan=2,pady=5, padx=3)
    treetime['columns'] = ('Column 2','Column 3')
    treetime.column("#0", width=50, minwidth=50)
    treetime.column("Column 2", width=150, minwidth=100)
    treetime.column("Column 3", width=90, minwidth=90)

    treetime.heading('#0', text='ID', anchor=W)
    treetime.heading('Column 2', text='Task', anchor=W)
    treetime.heading('Column 3', text='Date', anchor=W)

    header = ['Task', 'ID', ]
    i=1
    for record in records:
        Row = treetime.insert("",i,text=record[2], values=(record[0],record[1]))
        i=i+1


    # query_label = Label(root, text=tabulate(table, headers=header, tablefmt="grid"))
    # query_label.grid(row=7, column=0, columnspan=3, padx=10, pady=10 )
    # Commiting data
    conn.commit()
    
    # close connection
    conn.close()
    delete_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=95)
    delete_label.grid(row=5, column=0)
    delete_entry.grid(row=5, column=1, padx=20, )

#Entries
task_entry = Entry(root, width=30)
task_entry.grid(row=0, column=1, padx=20, pady=(10, 0))
date_entry = Entry(root, width=30)
date_entry.grid(row=1, column=1, padx=20, )
delete_entry = Entry(root, width=30)

# Labels
task_label = Label(root, text='Enter task:')
task_label.grid(row=0, column=0, pady=(10, 0))
date_label = Label(root, text='Enter Date:')
date_label.grid(row=1, column=0)
delete_label = Label(root, text=' ID number')

# Create Submit Button
submit_btn = Button(root, text='Add Task', command=submit)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=95)

# Create a Query button
query_btn = Button(root, text="Show task", command=query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=95)

# cREATE A DELETE BUTTON
delete_btn = Button(root, text="Delete task", command=delete_record)


# Commiting data
conn.commit()

# close connection
conn.close()







root.mainloop()