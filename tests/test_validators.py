"""Tests for input validation utilities."""

import unittest
from app.validators import validate_email, validate_password, validate_username


class TestEmailValidation(unittest.TestCase):
    """Test cases for email validation."""
    
    def test_valid_email(self):
        """Test validation of valid email addresses."""
        valid_emails = [
            "user@example.com",
            "test.user@example.co.uk",
            "user+tag@example.com",
            "user_123@example.com"
        ]
        
        for email in valid_emails:
            is_valid, error = validate_email(email)
            self.assertTrue(is_valid, f"Email {email} should be valid")
    
    def test_invalid_email_format(self):
        """Test validation of invalid email formats."""
        invalid_emails = [
            "invalid.email",
            "@example.com",
            "user@",
            "user name@example.com",
            "user@example"
        ]
        
        for email in invalid_emails:
            is_valid, error = validate_email(email)
            self.assertFalse(is_valid, f"Email {email} should be invalid")
    
    def test_empty_email(self):
        """Test validation of empty email."""
        is_valid, error = validate_email("")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Email cannot be empty")
    
    def test_email_too_long(self):
        """Test validation of overly long email."""
        long_email = "a" * 250 + "@example.com"
        is_valid, error = validate_email(long_email)
        self.assertFalse(is_valid)


class TestPasswordValidation(unittest.TestCase):
    """Test cases for password validation."""
    
    def test_valid_password(self):
        """Test validation of valid passwords."""
        valid_passwords = [
            "password123",
            "SecurePass456",
            "MyP@ssw0rd",
            "VeryLongPasswordWith123Numbers"
        ]
        
        for password in valid_passwords:
            is_valid, error = validate_password(password)
            self.assertTrue(is_valid, f"Password '{password}' should be valid")
    
    def test_password_too_short(self):
        """Test validation of passwords that are too short."""
        is_valid, error = validate_password("short")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Password must be at least 8 characters long")
    
    def test_empty_password(self):
        """Test validation of empty password."""
        is_valid, error = validate_password("")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Password cannot be empty")
    
    def test_password_too_long(self):
        """Test validation of passwords that are too long."""
        long_password = "a" * 129
        is_valid, error = validate_password(long_password)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Password is too long")


class TestUsernameValidation(unittest.TestCase):
    """Test cases for username validation."""
    
    def test_valid_username(self):
        """Test validation of valid usernames."""
        valid_usernames = [
            "user123",
            "test_user",
            "USER_NAME_123",
            "abc"
        ]
        
        for username in valid_usernames:
            is_valid, error = validate_username(username)
            self.assertTrue(is_valid, f"Username '{username}' should be valid")
    
    def test_username_too_short(self):
        """Test validation of usernames that are too short."""
        is_valid, error = validate_username("ab")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Username must be at least 3 characters")
    
    def test_username_too_long(self):
        """Test validation of usernames that are too long."""
        long_username = "a" * 33
        is_valid, error = validate_username(long_username)
        self.assertFalse(is_valid)
        self.assertEqual(error, "Username must be at most 32 characters")
    
    def test_username_invalid_characters(self):
        """Test validation of usernames with invalid characters."""
        invalid_usernames = [
            "user-name",
            "user name",
            "user@name",
            "user.name"
        ]
        
        for username in invalid_usernames:
            is_valid, error = validate_username(username)
            self.assertFalse(is_valid, f"Username '{username}' should be invalid")
    
    def test_empty_username(self):
        """Test validation of empty username."""
        is_valid, error = validate_username("")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Username cannot be empty")


if __name__ == "__main__":
    unittest.main()
