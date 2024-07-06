import tkinter as tk
from tkinter import ttk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

# Create the main window
root = tk.Tk()
root.title("Modern To-Do List")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Create a text entry field
entry = ttk.Entry(root, width=30)
entry.pack(pady=10)

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30, font=("Helvetica", 12))
listbox.pack()

# Create "Add" and "Remove" buttons
add_button = ttk.Button(root, text="Add", command=add_task)
add_button.pack()
remove_button = ttk.Button(root, text="Remove", command=remove_task)
remove_button.pack()

root.mainloop()