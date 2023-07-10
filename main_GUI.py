
import tkinter as tk
from tkinter import filedialog as fd
import tkinter.messagebox
from business_logic import CRUD
from tkinter import ttk
from pop_up import *

init_DB = CRUD()

window = tk.Tk()

# print(init_DB)

connection_on = False

# Set window properties
window.title("Window Title")
window.configure(bg="black")
window.resizable(False, False)  # Disable window resizing

# Calculate screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate x and y coordinates to center the window
window_width = 600
window_height = 600
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame to hold the labels and Entry fields
entry_frame = tk.Frame(window, bg="darkgray", pady=10)
entry_frame.pack(side="top", anchor="n", fill="x", padx=10, pady=(20, 10))

# Create the labels and Entry fields
label1 = tk.Label(entry_frame, text="Enter Name:", bg="darkgray")
entry1 = tk.Entry(entry_frame)

label2 = tk.Label(entry_frame, text="Enter Address:", bg="darkgray")
entry2 = tk.Entry(entry_frame)

# Position the labels and Entry fields using the grid manager
label1.grid(row=0, column=0, sticky="w", padx=5)
entry1.grid(row=1, column=0, sticky="we", padx=5)

label2.grid(row=0, column=1, sticky="w", padx=5)
entry2.grid(row=1, column=1, sticky="we", padx=5)

# Configure column weights for the entry_frame
entry_frame.columnconfigure(0, weight=1)
entry_frame.columnconfigure(1, weight=1)

def table():
    result = init_DB.get_all_people()

    if result:
        # Create the Treeview widget
        tree = ttk.Treeview(window)
        
        # Define columns
        tree["columns"] = ("ID", "NAME", "ADDRESS")
        
        # Format columns
        tree.column("#0", width=0, stretch=tk.NO)  # Hide the default first column
        tree.column("ID", width=50, stretch=True)
        tree.column("NAME", width=150, anchor=tk.W)
        tree.column("ADDRESS", width=200, anchor=tk.W)
        
        # Create headings
        tree.heading("ID", text="ID")
        tree.heading("NAME", text="NAME")
        tree.heading("ADDRESS", text="ADDRESS")
        
        # Insert data rows
        for row in result:
            row_tuple = tuple(row)  # Convert each row to a tuple
            tree.insert("", tk.END, values=row_tuple)
        
        # Pack the Treeview widget
        tree.pack(fill="both", expand=True)


# Create the button frame (remaining_frame)
remaining_frame = tk.Frame(window, bg="lightgray", pady=10)
remaining_frame.pack(side="bottom", anchor="n", fill="x", padx=10, pady=(10, 20))

#Clear entry fields
def clear_entry_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

def update_window():
    # Open a new window for updating records
    update_window = tk.Toplevel(window)
    update_window.title("Update Record")

    # Calculate x and y coordinates to center the update window
    update_window_width = 400
    update_window_height = 200
    x = (screen_width - update_window_width) // 2
    y = (screen_height - update_window_height) // 2
    update_window.geometry(f"{update_window_width}x{update_window_height}+{x}+{y}")

    # Create Entry fields for ID, Name, and Address
    id_label = tk.Label(update_window, text="ID:")
    id_entry = tk.Entry(update_window)
    name_label = tk.Label(update_window, text="Name:")
    name_entry = tk.Entry(update_window)
    address_label = tk.Label(update_window, text="Address:")
    address_entry = tk.Entry(update_window)

    # Grid positioning for the Entry fields and labels
    id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    id_entry.grid(row=0, column=1, padx=5, pady=5)
    name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    name_entry.grid(row=1, column=1, padx=5, pady=5)
    address_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    address_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a function to handle the update operation
    def perform_update():
        id = id_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        if not init_DB.update_person(name, address, id):
            tkinter.messagebox.showerror("Error", "Please click the Toggle Cnxn button first")
            update_window.destroy()
        else:
            update_window.destroy()
            tkinter.messagebox.showinfo("Success", "Record updated successfully!")


    # Create the Update button
    update_button = tk.Button(update_window, text="Update", bg="blue", fg="white", command=perform_update)
    update_button.grid(row=3, columnspan=2, padx=5, pady=5)


def delete_window():
    # Open a new window for deleting a record
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Record")

    # Calculate x and y coordinates to center the delete window
    delete_window_width = 400
    delete_window_height = 150
    x = (screen_width - delete_window_width) // 2
    y = (screen_height - delete_window_height) // 2
    delete_window.geometry(f"{delete_window_width}x{delete_window_height}+{x}+{y}")

    # Create Entry field for ID
    id_label = tk.Label(delete_window, text="ID:")
    id_entry = tk.Entry(delete_window)

    # Grid positioning for the Entry field and label
    id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    # Create a function to handle the delete operation
    def perform_delete():
        id = id_entry.get()
        init_DB.delete_by_id(id)
        delete_window.destroy()
        tkinter.messagebox.showinfo("Success", "User deleted successfully!")

    # Create the Delete button
    delete_button = tk.Button(delete_window, text="Delete", bg="red", fg="white", command=perform_delete)
    delete_button.grid(row=1, columnspan=2, padx=5, pady=5)


def Insert_Person():
    name = entry1.get()
    address = entry2.get()
    if name and address:
            init_DB.insert_person(name, address)
            clear_entry_fields()
            tkinter.messagebox.showinfo("Success", "User created successfully!")


# Create a label to display the connection status
connection_status_label = tk.Label(window, text="Database disconnected. Please click on the 'Toggle Cnxn Button' to start cnxn", fg="red")
connection_status_label.pack(fill="both")

    
def toggleMe():
    init_DB.toggle_connection()
    global connection_on
    connection_on = True
    if not connection_on:
        connection_status_label.config(text="Database disconnected. Please click on the 'Toggle Cnxn Button' to start cnxn")
    else:
        connection_status_label.config(text="Connection On!")


# Create the buttons
button1 = tk.Button(remaining_frame, text="Insert", bg="green", fg="white", width=10, command=Insert_Person)
button2 = tk.Button(remaining_frame, text="Update", bg="blue", fg="white", width=10, command=update_window)
button3 = tk.Button(remaining_frame, text="View", bg="yellow", fg="black", width=10, command=table)
button4 = tk.Button(remaining_frame, text="Delete", bg="red", fg="white", width=10, command=delete_window)
button5 = tk.Button(remaining_frame, text="Toggle Cnxn", bg="black", fg="white", width=10,
                   command=toggleMe)

# Position the buttons using the grid manager
button1.grid(row=0, column=0, padx=(0, 10))
button2.grid(row=0, column=1, padx=(0, 10))
button3.grid(row=0, column=2, padx=(0, 10))
button3.grid(row=0, column=2, padx=(0, 10))
button4.grid(row=0, column=3, padx=(0, 10))
button5.grid(row=0, column=4)

# Configure the remaining_frame for even horizontal spacing
remaining_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="equal")

window.mainloop()

