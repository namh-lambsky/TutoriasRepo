import pytest

import db_functions

def test_user_creation():
    id="1000000"
    email="jjaramillo@ucentral.edu.co"
    password="juegos.com"
    name="jean carlo jaramillo"
    account_type=1
    tutor_code=150
    assert db_functions.new_user(id,email,password,name,account_type,tutor_c=tutor_code)==True

def test_user_login():
    email="lcoltrane@ucentral.edu.co"
    password="juegos.com"
    assert db_functions.login(email,password)==True