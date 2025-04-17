import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("To-do List")

title = ttk.Label(window, text="To-do List", font=("Arial", 20))
title.grid(row=0, column=1)

subtitle = ttk.Label(window, text="Enter a task below:")
subtitle.grid(row=1, column=0)
taskEntry = ttk.Entry(window, width=50)
taskEntry.grid(row=1, column=1)

dueDate = ttk.Label(window, text="Due date (YYYY-MM-DD):")
dueDate.grid(row=2, column=0, sticky="e")
dueDateEntry = ttk.Entry(window, width=50)
dueDateEntry.grid(row=2, column=1)

tasks = []
taskListbox = tk.Listbox(window, width=50, height=10)
taskListbox.grid(row=3, column=1,)

def addTask():
    task = taskEntry.get()
    due = dueDateEntry.get()
    if task:
        fullTask = task + " - Due: " + (due if due else "N/A")
        tasks.append(fullTask)
        taskListbox.insert(tk.END, fullTask)
        taskEntry.delete(0, tk.END)
        dueDateEntry.delete(0, tk.END)
        print(tasks)
 
def deleteTask():
    tasks.remove(taskListbox.get(taskListbox.curselection()))
    taskListbox.delete(taskListbox.curselection())
    print(tasks)

def clearTasks():
    tasks.clear()
    taskListbox.delete(0, tk.END)
    print(tasks)

def dueDate(task):
    return task.split(" - Due: ")[1]
    
def sortByDue():
    tasks.sort(key=dueDate)
    taskListbox.delete(0, tk.END)
    for task in tasks:
        taskListbox.insert(tk.END, task)
    print(tasks)

ttk.Button(window, text="Add task", command=addTask).grid(row=4, column=1)
ttk.Button(window, text="Sort by due date", command=sortByDue).grid(row=4, column=2) 
ttk.Button(window, text="Delete task", command=deleteTask, ).grid(row=5, column=1)   
ttk.Button(window, text="Clear tasks", command=clearTasks).grid(row=5, column=2)

window.mainloop()