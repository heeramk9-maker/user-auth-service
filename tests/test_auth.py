"""Tests for authentication functionality."""

import unittest
from app.service import UserAuthenticationService


class TestUserAuthentication(unittest.TestCase):
    """Test cases for user authentication service."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.service = UserAuthenticationService()
    
    def test_register_user_success(self):
        """Test successful user registration."""
        success, message, user = self.service.register_user(
            "testuser",
            "test@example.com",
            "password123"
        )
        
        self.assertTrue(success)
        self.assertEqual(message, "User registered successfully")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
    
    def test_register_user_duplicate_username(self):
        """Test registration fails with duplicate username."""
        self.service.register_user("testuser", "test1@example.com", "password123")
        
        success, message, user = self.service.register_user(
            "testuser",
            "test2@example.com",
            "password456"
        )
        
        self.assertFalse(success)
        self.assertEqual(message, "Username already taken")
        self.assertIsNone(user)
    
    def test_register_user_duplicate_email(self):
        """Test registration fails with duplicate email."""
        self.service.register_user("user1", "test@example.com", "password123")
        
        success, message, user = self.service.register_user(
            "user2",
            "test@example.com",
            "password456"
        )
        
        self.assertFalse(success)
        self.assertEqual(message, "Email already registered")
        self.assertIsNone(user)
    
    def test_login_user_success(self):
        """Test successful user login."""
        self.service.register_user("testuser", "test@example.com", "password123")
        
        success, message, token = self.service.login_user("testuser", "password123")
        
        self.assertTrue(success)
        self.assertEqual(message, "Login successful")
        self.assertIsNotNone(token)
    
    def test_login_user_invalid_password(self):
        """Test login fails with invalid password."""
        self.service.register_user("testuser", "test@example.com", "password123")
        
        success, message, token = self.service.login_user("testuser", "wrongpassword")
        
        self.assertFalse(success)
        self.assertEqual(message, "Invalid username or password")
        self.assertIsNone(token)
    
    def test_login_user_nonexistent_user(self):
        """Test login fails for non-existent user."""
        success, message, token = self.service.login_user("nonexistent", "password123")
        
        self.assertFalse(success)
        self.assertEqual(message, "Invalid username or password")
        self.assertIsNone(token)
    
    def test_validate_session(self):
        """Test session validation."""
        self.service.register_user("testuser", "test@example.com", "password123")
        _, _, token = self.service.login_user("testuser", "password123")
        
        self.assertTrue(self.service.validate_session(token))
        self.assertFalse(self.service.validate_session("invalid_token"))
    
    def test_get_user_by_token(self):
        """Test retrieving user by session token."""
        self.service.register_user("testuser", "test@example.com", "password123")
        _, _, token = self.service.login_user("testuser", "password123")
        
        user = self.service.get_user_by_token(token)
        
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")
    
    def test_logout_user(self):
        """Test user logout."""
        self.service.register_user("testuser", "test@example.com", "password123")
        _, _, token = self.service.login_user("testuser", "password123")
        
        self.assertTrue(self.service.logout_user(token))
        self.assertFalse(self.service.validate_session(token))
    
    def test_get_user(self):
        """Test getting user by username."""
        self.service.register_user("testuser", "test@example.com", "password123")
        
        user = self.service.get_user("testuser")
        
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")


if __name__ == "__main__":
    unittest.main()
