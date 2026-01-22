"""User authentication service orchestration."""

from typing import Optional, Dict
from app.models import User
from app.validators import validate_email, validate_password, validate_username
from app.auth import hash_password, verify_password, generate_session_token


class UserAuthenticationService:
    """Service for managing user authentication and registration."""
    
    def __init__(self):
        """Initialize the authentication service."""
        self.users: Dict[str, User] = {}
        self.sessions: Dict[str, str] = {}
    
    def register_user(self, username: str, email: str, password: str) -> tuple:
        """Register a new user.
        
        Args:
            username: The desired username
            email: The user's email address
            password: The user's password
            
        Returns:
            Tuple of (success, message, user_object)
        """
        # Validate username
        is_valid, error = validate_username(username)
        if not is_valid:
            return False, error, None
        
        # Validate email
        is_valid, error = validate_email(email)
        if not is_valid:
            return False, error, None
        
        # Validate password
        is_valid, error = validate_password(password)
        if not is_valid:
            return False, error, None
        
        # Check if username already exists
        if username in self.users:
            return False, "Username already taken", None
        
        # Check if email already registered
        for user in self.users.values():
            if user.email == email:
                return False, "Email already registered", None
        
        # Create new user
        password_hash = hash_password(password)
        new_user = User(username, email, password_hash)
        self.users[username] = new_user
        
        return True, "User registered successfully", new_user
    
    def login_user(self, username: str, password: str) -> tuple:
        """Authenticate a user and create a session.
        
        Args:
            username: The username
            password: The password
            
        Returns:
            Tuple of (success, message, session_token)
        """
        # Validate inputs
        if not username or not password:
            return False, "Username and password required", None
        
        # Check if user exists
        if username not in self.users:
            return False, "Invalid username or password", None
        
        user = self.users[username]
        
        # Verify password
        if not verify_password(password, user.password_hash):
            return False, "Invalid username or password", None
        
        # Check if user is active
        if not user.is_active:
            return False, "User account is inactive", None
        
        # Generate session token
        session_token = generate_session_token(username)
        self.sessions[session_token] = username
        
        return True, "Login successful", session_token
    
    def validate_session(self, session_token: str) -> bool:
        """Validate if a session token is valid.
        
        Args:
            session_token: The session token to validate
            
        Returns:
            True if valid, False otherwise
        """
        return session_token in self.sessions
    
    def get_user_by_token(self, session_token: str) -> Optional[User]:
        """Get user associated with a session token.
        
        Args:
            session_token: The session token
            
        Returns:
            User object if valid, None otherwise
        """
        if session_token not in self.sessions:
            return None
        
        username = self.sessions[session_token]
        return self.users.get(username)
    
    def logout_user(self, session_token: str) -> bool:
        """Logout a user by invalidating their session.
        
        Args:
            session_token: The session token to invalidate
            
        Returns:
            True if successful, False otherwise
        """
        if session_token in self.sessions:
            del self.sessions[session_token]
            return True
        return False
    
    def get_user(self, username: str) -> Optional[User]:
        """Get a user by username.
        
        Args:
            username: The username
            
        Returns:
            User object if found, None otherwise
        """
        return self.users.get(username)
