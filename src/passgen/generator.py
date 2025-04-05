import secrets
import string

class PasswordGenerator:
    def __init__(self, length=14, include_uppercase=True, include_numbers=True, include_special_characters=True):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_numbers = include_numbers
        self.include_special_characters = include_special_characters
        
    def set_length(self, length):
        if not 14 <= length <= 64:
            raise ValueError("Password length must be between 14 and 64 characters.")
        self.length = length
    
    def generate(self):
        char_pool = string.ascii_lowercase

        if self.include_uppercase:
            char_pool += string.ascii_uppercase

        if self.include_numbers:
            char_pool += string.digits

        if self.include_special_characters:
            char_pool += string.punctuation

        if len(char_pool) == 0:
            raise ValueError("At least one character type must be selected.")

        password = "".join(secrets.choice(char_pool) for _ in range(self.length))
        return password
        

        
        