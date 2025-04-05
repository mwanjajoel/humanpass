# Passgen

**Passgen** is a Python package designed to generate secure, customizable passwords suitable for various applications.

## Features

- **Customizable Length**: Specify password lengths between 14 and 64 characters.
- **Character Inclusions**: Choose to include uppercase letters, numbers, and special characters.
- **Cryptographic Security**: Utilizes Python's `secrets` module for generating cryptographically secure passwords.

## Installation

Install passgen using pip:

```bash
pip install passgen
```

## Usage

```python
from passgen import PasswordGenerator

# Create a password generator with default settings
password_generator = PasswordGenerator()

# Generate a password
password = password_generator.generate()
```

You can also customize the password generator by setting the following parameters:

```python
from passgen import PasswordGenerator

# Create a password generator with custom settings
password_generator = PasswordGenerator(
    length=20,
    include_uppercase=True,
    include_numbers=True,
    include_special_characters=True
)

# Generate a password
password = password_generator.generate()
```
