import unittest
from app.model import User

class UserModelTestCase(unittest.TestCase)
	def test_password_setter(self):
		u = User(password = 'angie')
		self.assertTrue(u.password_hash is not None)

	def test_no_password_getter(self):
		u = User(password = 'angie')
		with self.assertRaises(AttributeError):
			u.password

	def test_password_verification(self):
		u = User(password = angie)
		self.assertTrue(u.verify_password('angie'))
		self.assertFalse(u.verify_password('angel'))

	def test_password_salts_are_random(self):
		u = User(password='angie')
		u2 = User(password='angie')
		self.assertTrue(u.password_hash != u2.password_hash)