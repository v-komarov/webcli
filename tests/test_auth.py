#coding:utf-8

import pytest
from src.auth import auth as login


def test_auth():
    """Checking of auth service"""
    assert login("none","none") == False
    
