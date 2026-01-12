"""
This module is to test app.py
"""
import pytest
from src.app import main

def test_user_input(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out =="Enter one of the following options"\
                           "1. top 100 players"\
                           "2. top 10 players"\
                           "3. player_nation"
