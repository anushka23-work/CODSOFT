import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import csv

from contact_manager import ContactManager
from storage import load_contacts, save_contacts
from utils import validate_phone, validate_email


class ContactBookGUI:

    def __init__(self, root):

        self.root = root

        self.root.title("Contact Book")
        self.root.geometry("1000x600")

        self.dark_mode = False

        self.manager = ContactManager()

        self.manager.contacts = load_contacts()

        self.create_widgets()

        self.refresh_contacts()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="📱 Contact Book",
            font=("Segoe UI", 20, "bold")
        )

        title.pack(pady=10)

        top_frame = tk.Frame(self.root)
        top_frame.pack(fill="x", padx=10)

        self.count_label = tk.Label(
            top_frame,
            text="Total Contacts: 0",
            font=("Segoe UI", 10, "bold")
        )

        self.count_label.pack(side="left")

        theme_btn = tk.Button(
            top_frame,
            text="🌙 Toggle Theme",
            command=self.toggle_theme
        )

        theme_btn.pack(side="right")

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left", padx=10, pady=10)

        tk.Label(left_frame, text="Name").pack()

        self.name_entry = ttk.Entry(left_frame, width=30)
        self.name_entry.pack()

        tk.Label(left_frame, text="Phone").pack()

        self.phone_entry = ttk.Entry(left_frame, width=30)
        self.phone_entry.pack()

        tk.Label(left_frame, text="Email").pack()

        self.email_entry = ttk.Entry(left_frame, width=30)
        self.email_entry.pack()

        tk.Label(left_frame, text="Address").pack()

        self.address_entry = ttk.Entry(left_frame, width=30)
        self.address_entry.pack()

        tk.Button(
            left_frame,
            text="Add Contact",
            command=self.add_contact
        ).pack(fill="x", pady=5)

        tk.Button(
            left_frame,
            text="Update Contact",
            command=self.update_contact
        ).pack(fill="x", pady=5)

        tk.Button(
            left_frame,
            text="Delete Contact",
            command=self.delete_contact
        ).pack(fill="x", pady=5)

        tk.Button(
            left_frame,
            text="Export CSV",
            command=self.export_csv
        ).pack(fill="x", pady=5)

        tk.Button(
            left_frame,
            text="Import CSV",
            command=self.import_csv
        ).pack(fill="x", pady=5)

        tk.Label(left_frame, text="Search").pack(pady=5)

        self.search_var = tk.StringVar()

        self.search_var.trace(
            "w",
            self.search_contacts
        )

        ttk.Entry(
            left_frame,
            textvariable=self.search_var
        ).pack()

        right_frame = tk.Frame(main_frame)

        right_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        columns = (
            "Name",
            "Phone",
            "Email",
            "Address"
        )

        self.tree = ttk.Treeview(
            right_frame,
            columns=columns,
            show="headings"
        )

        for col in columns:

            self.tree.heading(col, text=col)

            self.tree.column(
                col,
                width=180
            )

        self.tree.pack(
            fill="both",
            expand=True
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_contact
        )

    def add_contact(self):

        name = self.name_entry.get()

        phone = self.phone_entry.get()

        email = self.email_entry.get()

        address = self.address_entry.get()

        if not name:

            messagebox.showerror(
                "Error",
                "Name required"
            )

            return

        if not validate_phone(phone):

            messagebox.showerror(
                "Error",
                "Invalid Phone Number"
            )

            return

        if email and not validate_email(email):

            messagebox.showerror(
                "Error",
                "Invalid Email"
            )

            return

        contact = {

            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        self.manager.add_contact(contact)

        save_contacts(
            self.manager.contacts
        )

        self.refresh_contacts()

        self.clear_fields()

    def update_contact(self):

        selected = self.tree.focus()

        if not selected:
            return

        index = self.tree.index(selected)

        self.manager.update_contact(
            index,
            {
                "name": self.name_entry.get(),
                "phone": self.phone_entry.get(),
                "email": self.email_entry.get(),
                "address": self.address_entry.get()
            }
        )

        save_contacts(
            self.manager.contacts
        )

        self.refresh_contacts()

    def delete_contact(self):

        selected = self.tree.focus()

        if not selected:
            return

        index = self.tree.index(selected)

        self.manager.delete_contact(index)

        save_contacts(
            self.manager.contacts
        )

        self.refresh_contacts()

    def refresh_contacts(self):

        self.tree.delete(
            *self.tree.get_children()
        )

        for contact in self.manager.contacts:

            self.tree.insert(
                "",
                "end",
                values=(
                    contact["name"],
                    contact["phone"],
                    contact["email"],
                    contact["address"]
                )
            )

        self.count_label.config(
            text=f"Total Contacts: {len(self.manager.contacts)}"
        )

    def select_contact(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(
            selected,
            "values"
        )

        self.clear_fields()

        self.name_entry.insert(0, values[0])
        self.phone_entry.insert(0, values[1])
        self.email_entry.insert(0, values[2])
        self.address_entry.insert(0, values[3])

    def search_contacts(self, *args):

        query = self.search_var.get()

        result = self.manager.search_contact(query)

        self.tree.delete(
            *self.tree.get_children()
        )

        for contact in result:

            self.tree.insert(
                "",
                "end",
                values=(
                    contact["name"],
                    contact["phone"],
                    contact["email"],
                    contact["address"]
                )
            )

    def export_csv(self):

        file = filedialog.asksaveasfilename(
            defaultextension=".csv"
        )

        if file:

            with open(
                file,
                "w",
                newline=""
            ) as csvfile:

                writer = csv.writer(csvfile)

                writer.writerow(
                    [
                        "Name",
                        "Phone",
                        "Email",
                        "Address"
                    ]
                )

                for contact in self.manager.contacts:

                    writer.writerow(
                        [
                            contact["name"],
                            contact["phone"],
                            contact["email"],
                            contact["address"]
                        ]
                    )

    def import_csv(self):

        file = filedialog.askopenfilename(
            filetypes=[
                ("CSV Files", "*.csv")
            ]
        )

        if file:

            with open(file, "r") as csvfile:

                reader = csv.DictReader(
                    csvfile
                )

                for row in reader:

                    self.manager.add_contact(
                        {
                            "name": row["Name"],
                            "phone": row["Phone"],
                            "email": row["Email"],
                            "address": row["Address"]
                        }
                    )

            save_contacts(
                self.manager.contacts
            )

            self.refresh_contacts()

    def toggle_theme(self):

        if self.dark_mode:

            self.root.configure(
                bg="white"
            )

            self.dark_mode = False

        else:

            self.root.configure(
                bg="#2b2b2b"
            )

            self.dark_mode = True

    def clear_fields(self):

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)