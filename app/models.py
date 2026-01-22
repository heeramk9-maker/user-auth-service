"""Data models for user authentication service."""

from typing import Optional
from datetime import datetime


class User:
    """Represents a user in the system."""
    
    def __init__(self, username: str, email: str, password_hash: str):
        """Initialize a new user.
        
        Args:
            username: The username
            email: The email address
            password_hash: The hashed password
        """
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = datetime.now()
        self.is_active = True
    
    def __repr__(self) -> str:
        return f"<User(username='{self.username}', email='{self.email}')>"
