import unittest
from passgen.generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        generator = PasswordGenerator()
        password = generator.generate()
        self.assertEqual(len(password), 14)
    
    def test_custom_length(self):
        generator = PasswordGenerator(length=20)
        password = generator.generate()
        self.assertEqual(len(password), 20)
    
    def test_include_uppercase(self):
        generator = PasswordGenerator(include_uppercase=True)
        password = generator.generate()
        self.assertTrue(any(c.isupper() for c in password))
    
    def test_include_numbers(self):
        generator = PasswordGenerator(include_numbers=True)
        password = generator.generate()
        self.assertTrue(any(c.isdigit() for c in password))
    
    def test_include_special_characters(self):
        generator = PasswordGenerator(include_special_characters=True)
        password = generator.generate()
        self.assertTrue(any(c in string.punctuation for c in password))
    
    def test_all_character_types(self):
        generator = PasswordGenerator()
        password = generator.generate()
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))
    
    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            PasswordGenerator(length=13)
        with self.assertRaises(ValueError):
            PasswordGenerator(length=65)
    
    def test_set_length(self):
        generator = PasswordGenerator()
        generator.set_length(20)
        password = generator.generate()
        self.assertEqual(len(password), 20)
    
    def test_set_include_uppercase(self):
        generator = PasswordGenerator()
        generator.set_include_uppercase(True)
        password = generator.generate()
        self.assertTrue(any(c.isupper() for c in password))
    
    def test_set_include_numbers(self):
        generator = PasswordGenerator()
        generator.set_include_numbers(True)
        password = generator.generate()
        self.assertTrue(any(c.isdigit() for c in password))
    
    def test_set_include_special_characters(self):
        generator = PasswordGenerator()
        generator.set_include_special_characters(True)
        password = generator.generate()
        self.assertTrue(any(c in string.punctuation for c in password))
        
  
        
        