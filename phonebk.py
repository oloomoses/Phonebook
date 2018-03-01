class Phonebook:

	def __init__(self):
		self.phonebook = {}


	def add_contact(self, phone_no, name):
		self.phonebook[phone_no] = name
		return {"message" : "contact added successfully"}
		pass

	def view_contacts(self):
		self.phonebook = True
		return {'message' : 'you are now viewing the contacts'}
		pass	

	def update_contacts(self, phone_no, name):
		self.phonebook[phone_no] = name
		return {'message' : 'Information updated successfully'}
		pass

	def delete_contacts(self, phone_id):
		self.phonebook = phone_id
		return {'message' : 'contact deleted'}
		pass	