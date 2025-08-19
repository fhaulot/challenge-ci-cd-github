import os
import importlib

def run_app_with_env(env_value):
    os.environ["APP_ENV"] = env_value
    # recharge le module main.py avec la bonne variable
    if "main" in globals():
        importlib.reload(main)
    else:
        import main
    return main

def test_dev_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "Dev")
    import main
    assert "Dev" in main.env

def test_qa_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "QA")
    import main
    assert "QA" in main.env

def test_prod_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "Prod")
    import main
    assert "Prod" in main.env