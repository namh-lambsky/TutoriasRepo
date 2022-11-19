import mysql.connector
from mysql.connector import Error


class DAO:
    def __init__(self):
        try:
            self.tutorDB = mysql.connector.connect(
                host="bcrwnwdmzfbrjuiipd8p-mysql.services.clever-cloud.com",
                port="3306",
                user="ucnlpezbqcwms9nj",
                password="BP77gwGvGMv99ZdwY44J",
                database="bcrwnwdmzfbrjuiipd8p",
            )
        except Error as e:
            print(f"Error al intentar la conexión: {e}")

    # ------------------------------------------Función Create-------------------------------------
    def newObject(self, table, obj):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            if table == 0:
                try:
                    sqlInstruction = "INSERT INTO users(user_id, email, password, name, account_type_id) VALUES ('{0}','{1}','{2}','{3}','{4}')"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_user_id(),
                            obj.get_email(),
                            obj.get_password(),
                            obj.get_name(),
                            obj.get_account_type_id(),
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Nuevo usuario ingresado con exito!")
                except Error as e:
                    print(f"Error al crear el dato: {e}")
            elif table == 1:
                try:
                    sqlInstruction = "INSERT INTO students(rating, career_id,student_id) VALUES ('{0}','{1}','{2}')"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_rating(), obj.get_career_id(), obj.get_student_id()
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Nuevo estudiante ingresado con exito!")
                except Error as e:
                    print(f"Error al crear el dato: {e}")
            elif table == 2:
                try:
                    sqlInstruction = (
                        "INSERT INTO tutors(tutor_id, rating) VALUES ('{0}','{1}')"
                    )
                    cursor.execute(
                        sqlInstruction.format(obj.get_tutor_id(), obj.getRating())
                    )
                    self.tutorDB.commit()
                    print("¡Nuevo profesor ingresado con exito!")
                except Error as e:
                    print(f"Error al crear el dato: {e}")
            elif table == 3:
                try:
                    sqlInstruction = "INSERT INTO careers(id_career,career_name) VALUES ('{0}','{1}')"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_subject_id(), obj.get_name(), obj.get_career_id()
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Nueva materia ingresada con exito!")
                except Error as e:
                    print(f"Error al crear el dato: {e}")
            elif table == 4:
                try:
                    sqlInstruction = "INSERT INTO subjects(id_subject,name,id_career) VALUES ('{0}','{1}','{2}')"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_subject_id(), obj.get_name(), obj.get_career_id()
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Nueva materia ingresada con exito!")
                except Error as e:
                    print(f"Error al crear el dato: {e}")
            elif table == 5:
                try:
                    sqlInstruction = "INSERT INTO tutorships(schedule_id,subject_id,classroom_id,tutor_id ,student_id) VALUES ('{0}','{1}','{2}','{3}','{4}')"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_schedule_id(),
                            obj.get_subject_id(),
                            obj.get_classroom_id(),
                            obj.get_tutor_id(),
                            obj.get_student_id(),
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Nueva tutoría ingresada con exito!")
                except Error as e:
                    print(f"Error al crear el dato: {e}")
            elif table == 6:
                try:
                    sqlInstruction = "INSERT INTO schedule(id_schedule,schedule) VALUES ('{0}','{1}')"
                    cursor.execute(
                        sqlInstruction.format(obj.get_id_schedule(), obj.get_schedule())
                    )
                    self.tutorDB.commit()
                    print("¡Nuevo horario ingresado con exito!")
                except Error as e:
                    print(f"Error al crear el dato: {e}")
            elif table == 7:
                try:
                    sqlInstruction = "INSERT INTO classrooms(id_classroom,classroom_name) VALUES ('{0}','{1}')"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_id_classroom(), obj.get_classroom_name()
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Nuevo salon ingresado con exito!")
                except Error as e:
                    print(f"Error al crear el dato: {e}")

    # ------------------------------------------Función Read-------------------------------------
    def getTableInfo(self, table):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            if table == 0:
                try:
                    cursor.execute("SELECT * FROM users")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")
            elif table == 1:
                try:
                    cursor.execute("SELECT * FROM students")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")
            elif table == 2:
                try:
                    cursor.execute("SELECT * FROM tutors")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")
            elif table == 3:
                try:
                    cursor.execute("SELECT * FROM subjects")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")
            elif table == 4:
                try:
                    cursor.execute("SELECT * FROM careers")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")
            elif table == 5:
                try:
                    cursor.execute("SELECT * FROM tutorships")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")
            elif table == 6:
                try:
                    cursor.execute("SELECT * FROM schedule")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")
            elif table == 7:
                try:
                    cursor.execute("SELECT * FROM classrooms")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")
            elif table == 8:
                try:
                    cursor.execute("SELECT * FROM tutor_codes")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")

    def get_email(self, email):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins = "SELECT email FROM users where email='{0}'".format(email)
                cursor.execute(sql_ins)
                result = cursor.fetchone()
                return result
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_user_by_email(self, email):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins = "SELECT user_id, email, password, name, account_type_id FROM users WHERE email='{0}'".format(
                    email
                )
                cursor.execute(sql_ins)
                return dict(
                    zip(
                        ("user_id", "email", "password", "name", "account_type_id"),
                        cursor.fetchone(),
                    )
                )
            except Error as e:
                print(f"Error al intentar la conexión: {e}")
                return None

    def get_career_by_user_id(self, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins = (
                    "SELECT career_id FROM students where student_id='{0}'".format(id)
                )
                cursor.execute(sql_ins)
                result = cursor.fetchone()
                return result
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_user_by_account_type(self, account_type):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            try:
                sql_ins = "SELECT * FROM users where account_type_id='{0}'".format(
                    account_type
                )
                cursor.execute(sql_ins)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_tutorship(self, id_tutorship):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins = "SELECT * FROM tutorships where tutorship_id='{0}'".format(
                    id_tutorship
                )
                cursor.execute(sql_ins)
                return dict(
                    zip(
                        (
                            "tutorship_id",
                            "schedule_id",
                            "subject_id",
                            "classroom_id",
                            "tutor_id",
                            "student_id",
                        ),
                        cursor.fetchone(),
                    )
                )
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_subjects_by_career_id(self, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            try:
                sql_ins = "SELECT * FROM subjects where career_id='{0}'".format(id)
                cursor.execute(sql_ins)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_schedule_by_tutor_id(self, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            try:
                sql_ins = "SELECT * FROM tutor_subject_schedule_bridge where tutor_id='{0}'".format(
                    id
                )
                cursor.execute(sql_ins)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_tutor_by_subject_id(self, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            try:
                sql_ins = "SELECT tutor_id FROM tutor_subject_schedule_bridge where subject_id='{0}'".format(
                    id
                )
                cursor.execute(sql_ins)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_user_by_id(self, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins = "SELECT user_id, email, password, name, account_type_id FROM users WHERE user_id='{0}'".format(
                    id
                )
                cursor.execute(sql_ins)
                return dict(
                    zip(
                        ("user_id", "email", "password", "name", "account_type_id"),
                        cursor.fetchone(),
                    )
                )
            except Error as e:
                print(f"Error al intentar la conexión: {e}")
                return None

    def get_subject_by_id(self, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins = "SELECT subject_id, name, career_id FROM subjects WHERE subject_id='{0}'".format(
                    id
                )
                cursor.execute(sql_ins)
                return dict(
                    zip(
                        ("subject_id", "name", "career_id"),
                        cursor.fetchone(),
                    )
                )
            except Error as e:
                print(f"Error al intentar la conexión: {e}")
                return None

    def get_tutor_by_subject_id_inner(self, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            try:
                sql_ins = """
                    SELECT u.user_id, email, password, name, account_type_id
                    FROM tutor_subject_schedule_bridge tssb
                            LEFT JOIN users u ON u.user_id = tssb.tutor_id
                    WHERE tssb.subject_id = {0}
                """.format(
                    id
                )
                cursor.execute(sql_ins)
                return map(
                    lambda t: dict(
                        zip(
                            ("user_id", "email", "password", "name", "account_type_id"),
                            t,
                        )
                    ),
                    cursor.fetchall(),
                )
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_schedule_by_id(self, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins = "SELECT schedule_id, init_time, end_time, day FROM schedule WHERE schedule_id='{0}'".format(
                    id
                )
                cursor.execute(sql_ins)
                return dict(
                    zip(
                        ("schedule_id", "init_time", "end_time", "day"),
                        cursor.fetchone(),
                    )
                )
            except Error as e:
                print(f"Error al intentar la conexión: {e}")
                return None

    def get_classroom_by_id(self, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins = "SELECT id_classroom, classroom_name FROM classrooms WHERE id_classroom='{0}'".format(
                    id
                )
                cursor.execute(sql_ins)
                return dict(
                    zip(
                        ("id_classroom", "classroom_name"),
                        cursor.fetchone(),
                    )
                )
            except Error as e:
                print(f"Error al intentar la conexión: {e}")
                return None

    def get_schedule_by_subject_and_tutor(self, subject_id, tutor_id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            try:
                sql_ins = """
                    SELECT s.schedule_id, init_time, end_time, day
                    FROM tutor_subject_schedule_bridge tssb
                            LEFT JOIN schedule s on tssb.schedule_id = s.schedule_id
                    WHERE tssb.subject_id = {0}
                    AND tssb.tutor_id = {1}
                """.format(
                    subject_id, tutor_id
                )
                cursor.execute(sql_ins)
                return map(
                    lambda t: dict(
                        zip(("schedule_id", "init_time", "end_time", "day"), t)
                    ),
                    cursor.fetchall(),
                )
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_last_tutorship(self):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins = "SELECT * FROM tutorships WHERE tutorship_id=(SELECT max(tutorship_id) FROM tutorships);"
                cursor.execute(sql_ins)
                result = dict(
                    zip(
                        (
                            "tutorship_id",
                            "schedule_id",
                            "subject_id",
                            "classroom_id",
                            "tutor_id",
                            "student_id",
                        ),
                        cursor.fetchone(),
                    )
                )
                return result
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_tutorship_by_tutor_id(self, tutor_id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            try:
                sql_ins = """
                    SELECT * FROM tutorships WHERE tutor_id={0}
                """.format(
                    tutor_id
                )
                cursor.execute(sql_ins)
                return map(
                    lambda t: dict(
                        zip(
                            (
                                "tutorship_id",
                                "schedule_id",
                                "subject_id",
                                "classroom_id",
                                "tutor_id",
                                "student_id",
                            ),
                            t,
                        )
                    ),
                    cursor.fetchall(),
                )
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    # ------------------------------------------Función Update-------------------------------------
    def updateData(self, table, obj):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            if table == 0:
                try:
                    sqlInstruction = "UPDATE users SET email='{1}', password='{2}', account_type_id='{3}' WHERE user_id='{0}'"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_user_id(),
                            obj.get_email(),
                            obj.get_password(),
                            obj.get_account_type_id(),
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Usuario actualizado con exito!")
                except Error as e:
                    print(f"Error al actualizar el dato: {e}")
            elif table == 1:
                try:
                    sqlInstruction = "UPDATE students SET rating='{0}', career_id='{1}', student_id='{2}' WHERE student_id='{0}'"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_rating(), obj.get_career_id(), obj.get_student_id()
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Estudiante actualizado con exito!")
                except Error as e:
                    print(f"Error al actualizar el dato: {e}")
            elif table == 2:
                try:
                    sqlInstruction = "UPDATE tutors SET tutor_id='{0}', rating='{1}' WHERE tutor_id='{0}'"
                    cursor.execute(
                        sqlInstruction.format(obj.get_tutor_id(), obj.getRating())
                    )
                    self.tutorDB.commit()
                    print("¡Profesor actualizado con exito!")
                except Error as e:
                    print(f"Error al actualizar el dato: {e}")
            elif table == 3:
                try:
                    sqlInstruction = "UPDATE careers SET id_career='{0}', career_name='{1}' WHERE id_career='{0}'"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_id_career(), obj.get_career_name()
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Salon actualizada con exito!")
                except Error as e:
                    print(f"Error al actualizar el dato: {e}")
            elif table == 4:
                try:
                    sqlInstruction = "UPDATE subjects SET id_subject='{0}', name='{1}',id_career='{4}' WHERE id_subject='{0}'"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_subject_id(), obj.get_name(), obj.get_career_id()
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Materia actualizada con exito!")
                except Error as e:
                    print(f"Error al actualizar el dato: {e}")
            elif table == 5:
                try:
                    sqlInstruction = "UPDATE tutorships SET id_tutorship='{0}', student_email='{1}', id_subject='{2}', teacher_email='{3}' WHERE id_tutorship='{0}'"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_id_tutorship(),
                            obj.get_student_email(),
                            obj.get_id_subject(),
                            obj.id_classroom(),
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Tutoria actualizada con exito!")
                except Error as e:
                    print(f"Error al actualizar el dato: {e}")
            elif table == 6:
                try:
                    sqlInstruction = "UPDATE schedule SET id_schedule='{0}', schedule='{1}' WHERE id_schedule='{0}'"
                    cursor.execute(
                        sqlInstruction.format(obj.get_id_schedule(), obj.get_schedule())
                    )
                    self.tutorDB.commit()
                    print("¡Horario actualizada con exito!")
                except Error as e:
                    print(f"Error al actualizar el dato: {e}")
            elif table == 7:
                try:
                    sqlInstruction = "UPDATE classrooms SET id_classroom='{0}', classroom_name='{1}' WHERE id_classroom='{0}'"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_id_classroom(), obj.get_classroom_name()
                        )
                    )
                    self.tutorDB.commit()
                    print("¡Salon actualizada con exito!")
                except Error as e:
                    print(f"Error al actualizar el dato: {e}")

    # ------------------------------------------Función Delete-------------------------------------
    def deleteData(self, table, id):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            if table == 0:
                tableS = "users"
                id_type = "user_id"
            elif table == 1:
                tableS = "students"
                id_type = "student_id"
            elif table == 2:
                tableS = "tutor"
                id_type = "tutor_id"
            elif table == 3:
                tableS = "careers"
                id_type = "id_career"
            elif table == 4:
                tableS = "subjects"
                id_type = "id_subject"
            elif table == 5:
                tableS = "tutorships"
                id_type = "tutorship_id"
            elif table == 6:
                tableS = "schedule"
                id_type = "id_schedule"
            elif table == 7:
                tableS = "classrooms"
                id_type = "id_classroom"
            try:
                sqlInstruction = "DELETE FROM {0} WHERE {1} = '{2}' "
                cursor.execute(sqlInstruction.format(tableS, id_type, id))
                self.tutorDB.commit()
                print(f"Borro de la tabla{tableS} dato{id_type}={id}")
            except Error as e:
                print(f"Error al actualizar el dato: {e}")
