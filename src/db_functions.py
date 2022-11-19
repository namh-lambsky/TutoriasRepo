from db_connector import DAO
from user import User
from student import Student
from tutor import Tutor
from tutorship import Tutorship

db = DAO()


def new_tutorship(schedule_id, subject_id, classroom_id, tutor_id, student_id):
    tutorship = Tutorship(schedule_id, subject_id, classroom_id, tutor_id, student_id)
    db.newObject(5, tutorship)


def new_user(id, email, password, name, account_type, career_id=0, tutor_c=0):
    tutor_code_exists = False
    user = User(int(id), email, password, name, int(account_type))
    db.newObject(0, user)
    if account_type == 1:
        student = Student(5, career_id, id)
        db.newObject(1, student)
        return True
    elif account_type == 2:
        tutor_codes = db.getTableInfo(8)
        for tutor_code in tutor_codes:
            if tutor_code[0] == int(tutor_c):
                tutor_code_exists = True
                break
        if tutor_code_exists:
            tutor = Tutor(id, 5)
        else:
            tutor = None
            return False
        db.newObject(2, tutor)
        return True


def login(email, password):
    user = db.get_user_by_email(email)
    if user is None:
        return None

    if user["password"] != password:
        return None
    else:
        return user


def get_table(num):
    lista = db.getTableInfo(num)
    return lista


def email_exists(email):
    email_db = db.get_email(email)
    if email_db is None:
        return False
    else:
        if email_db[0] == email:
            return True


def get_user_by_id(id):
    return db.get_user_by_id(id)


def get_users_by_type(type):
    lista = db.get_user_by_account_type(type)
    return lista


def get_schedule_by_id(id):
    return db.get_schedule_by_id(id)


def get_classroom_by_id(id):
    return db.get_classroom_by_id(id)


def get_career_by_user_id(id):
    return db.get_career_by_user_id(id)


def get_subjects_by_career_id(id):
    subjects = db.get_subjects_by_career_id(id)
    return subjects


def get_schedule_by_tutor_id(id):
    schedule = db.get_schedule_by_tutor_id(id)
    return schedule


def get_tutor_by_subject_id(id):
    tutor = db.get_tutor_by_subject_id_inner(id)
    return tutor


def get_schedule_by_subject_and_tutor(subject_id, tutor_id):
    schedule = db.get_schedule_by_subject_and_tutor(subject_id, tutor_id)
    return schedule


def get_tutorship(id):
    summary = db.get_tutorship(id)
    return summary


def get_last_tutorship():
    return db.get_last_tutorship()


def get_subject_by_id(id):
    return db.get_subject_by_id(id)


def delete_by_id(table, id):
    return db.deleteData(table, id)


def get_tutorship_by_tutor_id(id):
    return db.get_tutorship_by_tutor_id(id)