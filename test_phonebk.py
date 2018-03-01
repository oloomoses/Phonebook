import unittest
from phonebk import Phonebook

class PhonebookTestCase(unittest.TestCase):

	def test_add_contacts(self):
		phonebk = Phonebook()
		response = phonebk.add_contact('003344', 'Moses')
		self.assertEqual(response["message"], "contact added successfully")
		

	def test_view_contact(self):
		phonebk = Phonebook()
		response = phonebk.view_contacts()
		self.assertEqual(response['message'], 'you are now viewing the contacts')
		

	def test_delete_contacts(self):
		phonebk = Phonebook()
		response = phonebk.delete_contacts('32')
		self.assertEqual(response['message'], 'contact deleted')
		

	def test_update_contacts(self):
		phonebk = Phonebook()
		response = phonebk.update_contacts('038345', 'john')
		self.assertEqual(response['message'], 'Information updated successfully')
		
		



