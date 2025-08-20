import os
import pytest
import sys  # Import the sys module
import importlib

def test_dev_environment(monkeypatch):
    """
    Tests the application in the 'Dev' environment.
    """
    # Remove the module from the cache to ensure a clean import
    if "app.main" in sys.modules:
        del sys.modules["app.main"]
        
    monkeypatch.setenv("APP_ENV", "Dev")
    import app.main
    assert "Dev" in app.main.env

def test_qa_environment(monkeypatch):
    """
    Tests the application in the 'QA' environment.
    """
    # Remove the module from the cache to ensure a clean import
    if "app.main" in sys.modules:
        del sys.modules["app.main"]
        
    monkeypatch.setenv("APP_ENV", "QA")
    import app.main
    assert "QA" in app.main.env

def test_prod_environment(monkeypatch):
    """
    Tests the application in the 'Prod' environment.
    """
    # Remove the module from the cache to ensure a clean import
    if "app.main" in sys.modules:
        del sys.modules["app.main"]
        
    monkeypatch.setenv("APP_ENV", "Prod")
    import app.main
    assert "Prod" in app.main.env