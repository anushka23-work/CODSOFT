import tkinter as tk
from tkinter import ttk, messagebox
from contact_manager import ContactManager
from storage import load_contacts, save_contacts
from utils import validate_phone, validate_email

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book Pro")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f0f2f5")

        self.manager = ContactManager()
        self.manager.contacts = load_contacts()
        self.create_widgets()
        self.refresh_contacts()

    def create_widgets(self):
        # Header
        title = tk.Label(self.root, text="📱 My Contact Book", font=("Segoe UI", 24, "bold"), 
                         bg="#4a90e2", fg="white", pady=15)
        title.pack(fill="x")

        main_frame = tk.Frame(self.root, bg="#f0f2f5")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Input Frame
        left_frame = tk.LabelFrame(main_frame, text="Details", font=("Arial", 12, "bold"), 
                                   bg="#ffffff", padx=15, pady=15, relief="flat")
        left_frame.pack(side="left", fill="y", padx=(0, 20))

        # Fields
        for label_text, var in [("Name:", "name"), ("Phone:", "phone"), ("Email:", "email"), ("Address:", "address")]:
            tk.Label(left_frame, text=label_text, bg="white", font=("Arial", 10)).pack(anchor="w")
            entry = ttk.Entry(left_frame, width=30)
            entry.pack(pady=(0, 10))
            setattr(self, f"{var}_entry", entry)

        # Buttons
        tk.Button(left_frame, text="Add Contact", command=self.add_contact, bg="#28a745", fg="white", font=("Arial", 9, "bold"), width=20, relief="flat").pack(pady=5)
        tk.Button(left_frame, text="Update", command=self.update_contact, bg="#ffc107", font=("Arial", 9, "bold"), width=20, relief="flat").pack(pady=5)
        tk.Button(left_frame, text="Delete", command=self.delete_contact, bg="#dc3545", fg="white", font=("Arial", 9, "bold"), width=20, relief="flat").pack(pady=5)

        # Treeview
        right_frame = tk.Frame(main_frame, bg="#f0f2f5")
        right_frame.pack(side="right", fill="both", expand=True)

        self.tree = ttk.Treeview(right_frame, columns=("Name", "Phone", "Email", "Address"), show="headings")
        for col in ("Name", "Phone", "Email", "Address"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.select_contact)
        
        self.count_label = tk.Label(right_frame, text="Total Contacts: 0", font=("Arial", 10, "bold"), bg="#f0f2f5")
        self.count_label.pack(pady=5)

    def refresh_contacts(self):
        self.tree.delete(*self.tree.get_children())
        for contact in self.manager.contacts:
            self.tree.insert("", "end", values=(contact["name"], contact["phone"], contact["email"], contact.get("address", "N/A")))
        self.count_label.config(text=f"Total Contacts: {len(self.manager.contacts)}")

    def add_contact(self):
        name, phone, email, address = self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.address_entry.get()
        if not name or not validate_phone(phone) or (email and not validate_email(email)):
            messagebox.showerror("Error", "Invalid Input! Check Name, Phone, and Email.")
            return
        self.manager.add_contact({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts(self.manager.contacts)
        self.refresh_contacts()
        self.clear_fields()

    def update_contact(self):
        selected = self.tree.focus()
        if selected:
            index = self.tree.index(selected)
            self.manager.update_contact(index, {"name": self.name_entry.get(), "phone": self.phone_entry.get(), "email": self.email_entry.get(), "address": self.address_entry.get()})
            save_contacts(self.manager.contacts)
            self.refresh_contacts()

    def delete_contact(self):
        selected = self.tree.focus()
        if selected:
            self.manager.delete_contact(self.tree.index(selected))
            save_contacts(self.manager.contacts)
            self.refresh_contacts()
            self.clear_fields()

    def select_contact(self, event):
        selected = self.tree.focus()
        if selected:
            vals = self.tree.item(selected, "values")
            self.clear_fields()
            self.name_entry.insert(0, vals[0]); self.phone_entry.insert(0, vals[1])
            self.email_entry.insert(0, vals[2]); self.address_entry.insert(0, vals[3])

    def clear_fields(self):
        for entry in [self.name_entry, self.phone_entry, self.email_entry, self.address_entry]:
            entry.delete(0, tk.END)