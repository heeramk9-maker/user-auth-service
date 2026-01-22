# User Authentication Service

A simple, in-memory user authentication service built with Python. This service provides user registration, login, session management, and input validation.

## Features

- User registration with email validation
- User login with password verification
- Session token management
- Input validation for username, email, and password
- User account status management
- In-memory user storage

## Requirements

- Python 3.8 or higher

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/user-auth-service.git
cd user-auth-service
```

2. (Optional) Create a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from app.service import UserAuthenticationService

# Create service instance
auth_service = UserAuthenticationService()

# Register a new user
success, message, user = auth_service.register_user(
    username="john_doe",
    email="john@example.com",
    password="SecurePassword123"
)

if success:
    print(f"User registered: {user}")
else:
    print(f"Registration failed: {message}")

# Login user
success, message, token = auth_service.login_user(
    username="john_doe",
    password="SecurePassword123"
)

if success:
    print(f"Login successful. Token: {token}")
else:
    print(f"Login failed: {message}")

# Validate session
if auth_service.validate_session(token):
    print("Session is valid")

# Get user by token
user = auth_service.get_user_by_token(token)
print(f"Current user: {user}")

# Logout
auth_service.logout_user(token)
```

## Running Tests

Run all tests:
```bash
python -m pytest tests/
```

Or using unittest:
```bash
python -m unittest discover tests/
```

Run specific test file:
```bash
python -m unittest tests.test_auth
```

Run specific test:
```bash
python -m unittest tests.test_auth.TestUserAuthentication.test_register_user_success
```

## Project Structure

```
user-auth-service/
├── app/
│   ├── __init__.py           # Package initialization
│   ├── models.py             # User model definition
│   ├── validators.py         # Input validation functions
│   ├── auth.py              # Authentication utilities
│   └── service.py           # Main authentication service
├── tests/
│   ├── __init__.py
│   ├── test_auth.py         # Authentication tests
│   └── test_validators.py   # Validation tests
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## API Reference

### UserAuthenticationService

#### `register_user(username, email, password) -> (success, message, user)`
Register a new user in the system.

**Parameters:**
- `username` (str): The desired username (3-32 characters, alphanumeric and underscores)
- `email` (str): The user's email address (valid email format)
- `password` (str): The user's password (min 8, max 128 characters)

**Returns:**
- `success` (bool): Whether registration was successful
- `message` (str): Status or error message
- `user` (User or None): The created user object or None if failed

#### `login_user(username, password) -> (success, message, token)`
Authenticate a user and create a session.

**Parameters:**
- `username` (str): The username
- `password` (str): The password

**Returns:**
- `success` (bool): Whether login was successful
- `message` (str): Status or error message
- `token` (str or None): Session token or None if failed

#### `validate_session(session_token) -> bool`
Check if a session token is valid.

#### `get_user_by_token(session_token) -> User or None`
Get the user associated with a valid session token.

#### `logout_user(session_token) -> bool`
Invalidate a session token.

#### `get_user(username) -> User or None`
Retrieve a user by username.

## Validation Rules

### Username
- Must be 3-32 characters long
- Can only contain letters, numbers, and underscores
- Must be unique in the system

### Email
- Must be a valid email format
- Must be unique in the system
- Maximum 254 characters

### Password
- Must be 8-128 characters long
- Stored as SHA-256 hash (for demonstration purposes)

## Security Notes

⚠️ **This is a demonstration project** and should NOT be used in production. 

Key limitations:
- Passwords are hashed with SHA-256 (use bcrypt in production)
- Session tokens are simple and not cryptographically secure (use JWT in production)
- No database persistence (use PostgreSQL/MongoDB in production)
- No rate limiting or brute force protection
- No HTTPS/TLS enforcement

For production systems, implement:
- Use bcrypt or Argon2 for password hashing
- Implement JWT with proper expiration
- Add database persistence with encryption
- Implement rate limiting and account lockout
- Use HTTPS/TLS for all communications
- Add two-factor authentication

## License

MIT License

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request.
