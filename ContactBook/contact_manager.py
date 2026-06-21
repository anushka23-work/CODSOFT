class ContactManager:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def update_contact(self, index, contact):
        self.contacts[index] = contact

    def delete_contact(self, index):
        del self.contacts[index]

    def get_contacts(self):
        return self.contacts

    def search_contact(self, query):

        query = query.lower()

        return [
            contact for contact in self.contacts
            if query in contact["name"].lower()
            or query in contact["phone"]
        ]