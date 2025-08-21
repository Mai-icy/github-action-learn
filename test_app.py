# test_app.py
from app import print_hi

def test_greet():
    assert print_hi("GitHub Actions") == "Hi, GitHub Actions!"
