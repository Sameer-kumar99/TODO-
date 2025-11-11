# tests/conftest.py
"""
Pytest configuration and shared fixtures for tests.
"""
import pytest
from app.app import app, service

@pytest.fixture(autouse=True)
def reset_service():
    """Reset the service state before and after each test."""
    # Save original state
    original_tasks = service.tasks.copy() if service.tasks else []
    original_next_id = service.next_id
    
    # Reset before test
    service.tasks = []
    service.next_id = 1
    
    yield
    
    # Reset after test
    service.tasks = []
    service.next_id = 1

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    return app.test_client()

