import pytest
import datetime
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
    assert db_functions.login(email,password)==None
    
def test_set_item_schedule():
    schedule={"schedule_id":1,"init_time":datetime.timedelta(seconds=28800),
              "end_time":datetime.timedelta(seconds=30600),"day":"lun"}
    assert db_functions.get_schedule_by_id(1)==schedule
    
def test_set_item_subject():
    subject={"subject_id":1,"name":"IngenierÃ­a de software I","career_id":1}
    assert db_functions.get_subject_by_id(1)==subject

def test_set_item_tutor():
    tutor={"user_id":1,"email":"jpmozan@ucentral.edu.co","password":"siuuuu1012",
           "name":"juan pablo mozambique","account_type_id":2}
    assert list(db_functions.get_tutor_by_subject_id(1))[0]==tutor
    
def test_set_item_aula():
    aula={"id_classroom":1,"classroom_name":"Nuevo campus, aula 602"}
    assert db_functions.get_classroom_by_id(1)==aula

def test_set_tutorships():
    tutorship={"tutorship_id":19,
                            "schedule_id":3,
                            "subject_id":1,
                            "classroom_id":2,
                            "tutor_id":2131451,
                            "student_id":1001299657}
    assert db_functions.get_tutorship(19)==tutorship