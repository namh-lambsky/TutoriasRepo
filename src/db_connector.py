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
                    sqlInstruction = "INSERT INTO tutorships(id_subject,name,topics,teacher_email) VALUES ('{0}','{1}','{2}','{3}')"
                    cursor.execute(
                        sqlInstruction.format(
                            obj.get_id_subject(),
                            obj.get_name(),
                            obj.get_topics(),
                            obj.get_teacher_email(),
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
            elif table ==8:
                try:
                    cursor.execute("SELECT * FROM tutor_codes")
                    result = cursor.fetchall()
                    return result
                except Error as e:
                    print(f"Error al intentar la conexión: {e}")

    def get_password_by_email(self,email):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor()
            try:
                sql_ins="SELECT password FROM users where email='{0}'".format(email)
                cursor.execute(sql_ins)
                result = cursor.fetchone()
                return result
            except Error as e:
                print(f"Error al intentar la conexión: {e}")

    def get_email(self,email):
        if self.tutorDB.is_connected():
            cursor = self.tutorDB.cursor(buffered=True)
            try:
                sql_ins="SELECT email FROM users where email='{0}'".format(email)
                cursor.execute(sql_ins)
                result = cursor.fetchone()
                return result
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
                id_type = "id_tutorship"
            elif table == 6:
                tableS = "schedule"
                id_type = "id_schedule"
            elif table == 7:
                tableS = "classrooms"
                id_type = "id_classroom"
            try:
                sqlInstruction = "DELETE FROM '{0}' WHERE '{1}' = '{2}' "
                cursor.execute(sqlInstruction.format(tableS, id_type, id))
                self.tutorDB.commit()
                print("¡Cliente eliminado con exito!")
            except Error as e:
                print(f"Error al actualizar el dato: {e}")
