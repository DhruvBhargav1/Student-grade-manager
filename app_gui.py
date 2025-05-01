import tkinter as tk
from tkinter import messagebox
from student_management import add_student, del_student, get_all_student

# Function to add a student using GUI
def gui_add_student():
    name = entry_name.get()  # Get name from input field
    grade = entry_grade.get()  # Get grade from input field

    success, message = add_student(name, grade)  # Call backend function

    if success:
        entry_name.delete(0, tk.END)  # Clear name field
        entry_grade.delete(0, tk.END)  # Clear grade field
        update_listbox()  # Refresh the listbox
        messagebox.showinfo("Success", message)  # Show success popup
    else:
        messagebox.showerror("Error", message)  # Show error popup

# Function to delete selected student from listbox
def gui_delete_student():
    selected = listbox.curselection()  # Get selected item index

    if selected:
        item = listbox.get(selected)  # Get selected item text
        name = item.split(":")[0]  # Extract name from "name:grade" format

        success, message = del_student(name)  # Call backend function
        update_listbox()  # Refresh listbox

        if success:
            messagebox.showinfo("Deleted", message)
        else:
            messagebox.showerror("Error", message)
    else:
        messagebox.showwarning("Warning", "No student selected")

# Function to refresh listbox with current student data
def update_listbox():
    listbox.delete(0, tk.END)  # Clear current listbox

    for name, grade in get_all_student().items():  # Get student data
        listbox.insert(tk.END, f"{name}:{grade}")  # Add to listbox

# GUI Window Setup
root = tk.Tk()  # Create window
root.title("Student Grade Management")
root.geometry("300x400")  # Set size (not 300*400)

# Name input
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Grade input
tk.Label(root, text="Grade:").pack()
entry_grade = tk.Entry(root)
entry_grade.pack()

# Buttons
tk.Button(root, text="Add Student", command=gui_add_student).pack(pady=5)
tk.Button(root, text="Delete Selected", command=gui_delete_student).pack(pady=5)

# Listbox to display students
listbox = tk.Listbox(root)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Run GUI
root.mainloop()
