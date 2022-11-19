from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
import re
import db_functions as func

Window.size = (412, 800)


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    helper_text = StringProperty()


class MD3Card(MDCard):
    text = StringProperty()


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class GUI(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "700"
        carrer_list = func.get_table(4)
        self.account_type = None
        self.pass_verifier = False
        self.id_verifier = False
        self.email_verifier = False
        self.tutor_id = None
        self.tutor_code = None
        self.dialog = None
        self.carrera = func.get_table(4)
        self.user_id_del = None

        self.dpdown_user_type_items = [
            {
                "viewclass": "IconListItem",
                "icon": "account",
                "text": "Maestro",
                "height": dp(56),
                "on_release": lambda x="Maestro": self.set_item_user(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "account-school",
                "text": "Estudiante",
                "height": dp(56),
                "on_release": lambda x="Estudiante": self.set_item_user(x),
            },
        ]
        self.dpdown_career_items = [
            {
                "viewclass": "IconListItem",
                "icon": "book-education",
                "text": f"{i[1]}",
                "height": dp(56),
                "on_release": lambda x=f"{i[1]}": self.set_item_career(x),
            }
            for i in self.carrera
        ]

        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Builder.load_file("style/main.kv"))
        self.screen_manager.add_widget(Builder.load_file("style/login.kv"))
        self.screen_manager.add_widget(Builder.load_file("style/signup.kv"))
        self.menu = MDDropdownMenu(
            caller=self.screen_manager.get_screen("signup").ids.usertype,
            items=self.dpdown_user_type_items,
            width_mult=3,
        )
        self.menu_career = MDDropdownMenu(
            caller=self.screen_manager.get_screen("signup").ids.career_list,
            ver_growth="up",
            hor_growth="right",
            items=self.dpdown_career_items,
            width_mult=8,
        )
        self.menu_career.bind()
        return self.screen_manager

    def clear_signup(self):
        self.screen_manager.get_screen("signup").ids.newnombre.text = ""
        self.screen_manager.get_screen("signup").ids.newemail.text = ""
        self.screen_manager.get_screen(
            "signup"
        ).ids.newpassword.ids.text_field.text = ""
        self.screen_manager.get_screen(
            "signup"
        ).ids.verifypassword.ids.text_field.text = ""
        self.screen_manager.get_screen("signup").ids.cedula.text = ""
        self.screen_manager.get_screen("signup").ids.code.text = ""
        self.screen_manager.get_screen("signup").ids.usertype.text = ""
        self.screen_manager.get_screen("signup").ids.career_list.text = ""
        self.screen_manager.get_screen("signup").ids.code.text = ""

    def set_item_user(self, text_item):
        self.screen_manager.get_screen("signup").ids.usertype.text = text_item
        self.screen_manager.get_screen("signup").ids.career_list.pos = (-6000, 110)
        self.screen_manager.get_screen("signup").ids.code.pos = (-6000, 110)
        if text_item == "Estudiante":
            self.screen_manager.get_screen("signup").ids.career_list.pos = (60, 110)
            self.account_type = 1
        elif text_item == "Maestro":
            self.screen_manager.get_screen("signup").ids.code.pos = (60, 110)
            self.account_type = 2
        self.menu.dismiss()

    def set_item_career(self, text_item):
        self.screen_manager.get_screen("signup").ids.career_list.text = text_item
        self.career_id = None
        if text_item == "Ingeniería de Sistemas":
            self.career_id = 1
        elif text_item == "Ingeniería Electrónica":
            self.career_id = 2
        elif text_item == "Ingeniería Industrial":
            self.career_id = 3
        else:
            print("no entre a ningun caso")
        self.menu_career.dismiss()

    def show_alert_dialog(self, text):
        if not self.dialog:
            self.dialog = MDDialog(
                text=text,
                buttons=[
                    MDFlatButton(
                        text="Intentar de nuevo",
                        theme_text_color="Custom",
                        on_release=self.close_dialog,
                    )
                ],
            )
        self.dialog.open()

    def close_dialog(self, ob):
        self.dialog.dismiss()

    def is_empty(self, text):
        if text == "" or " ":
            return True
        else:
            return False

    def valid_id(self, cedula):
        id_pattern = re.compile(r"[0-9]{6,11}")
        if re.fullmatch(id_pattern, cedula):
            self.id_verifier = True
        else:
            self.id_verifier = False
            self.screen_manager.get_screen(
                "signup"
            ).ids.cedula.helper_text = "La cedula debe contener entre 6 y 11 carácteres"
            self.screen_manager.get_screen("signup").ids.cedula.error = True

    def verify_email_signup(self, email):
        emailConfirmPattern = re.compile(r"^[A-Za-z0-9]+@ucentral\.edu\.co$")
        if re.fullmatch(emailConfirmPattern, email):
            if self.email_exists(email):
                self.email_verifier = False
                self.screen_manager.get_screen(
                    "signup"
                ).ids.newemail.helper_text = (
                    "el correo ya fue utilizado en otra cuenta!"
                )
                self.screen_manager.get_screen("signup").ids.newemail.error = True
            else:
                self.email_verifier = True
        else:
            self.email_verifier = False
            self.screen_manager.get_screen(
                "signup"
            ).ids.newemail.helper_text = (
                "El correo instucional debe ser correo@ucentral.edu.co"
            )
            self.screen_manager.get_screen("signup").ids.newemail.error = True

    def verify_password_signup(self, verifypass1, verifypass2):
        if verifypass1 == verifypass2:
            self.pass_verifier = True
        else:
            self.pass_verifier = False
            self.screen_manager.get_screen(
                "signup"
            ).ids.verifypassword.helper_text = "Las contraseñas no coinciden"
            self.screen_manager.get_screen(
                "signup"
            ).ids.verifypassword.ids.text_field.error = True

    def save_data_signup(self):
        nombre = self.screen_manager.get_screen("signup").ids.newnombre.text
        email = self.screen_manager.get_screen("signup").ids.newemail.text
        verifypass1 = self.screen_manager.get_screen(
            "signup"
        ).ids.newpassword.ids.text_field.text
        verifypass2 = self.screen_manager.get_screen(
            "signup"
        ).ids.verifypassword.ids.text_field.text
        cedula = self.screen_manager.get_screen("signup").ids.cedula.text
        codeT = self.screen_manager.get_screen("signup").ids.code.text

        self.tutor_code = codeT
        self.verify_email_signup(email)
        self.verify_password_signup(verifypass1, verifypass2)
        self.valid_id(cedula)
        if self.pass_verifier and self.id_verifier and self.email_verifier:
            if self.account_type == 1:
                func.new_user(
                    cedula,
                    email,
                    verifypass1,
                    nombre,
                    self.account_type,
                    career_id=self.career_id,
                )
                self.clear_signup()
                self.screen_manager.transition.direction = "left"
                self.screen_manager.current = "main"
                return True
            elif self.account_type == 2:
                func.new_user(
                    cedula,
                    email,
                    verifypass1,
                    nombre,
                    self.account_type,
                    tutor_c=self.tutor_code,
                )
                self.clear_signup()
                self.screen_manager.transition.direction = "left"
                self.screen_manager.current = "main"
                return True
        else:
            return False

    def email_exists(self, email):
        return func.email_exists(email)

    # ---Login----
    def clear_login(self):
        self.screen_manager.get_screen("login").ids.emailEstablecido.text = ""
        self.screen_manager.get_screen(
            "login"
        ).ids.passwordEstablecida.ids.text_field.text = ""

    def verify_email_login(self):
        emailConfirmPattern = re.compile(r"^[A-Za-z0-9]+@ucentral\.edu\.co$")
        text = self.screen_manager.get_screen("login").ids.emailEstablecido.text
        if re.fullmatch(emailConfirmPattern, text):
            self.verifier = True
        else:
            self.verifier = False
            self.screen_manager.get_screen(
                "login"
            ).ids.emailEstablecido.helper_text = (
                "El correo instucional debe ser (ej. correo@ucentral.edu.co)"
            )
            self.screen_manager.get_screen("login").ids.emailEstablecido.error = True

    def save_data_login(self):
        email_log = self.screen_manager.get_screen("login").ids.emailEstablecido.text
        password_log = self.screen_manager.get_screen(
            "login"
        ).ids.passwordEstablecida.ids.text_field.text
        self.verify_email_login()
        if self.verifier:
            self.user = func.login(email_log, password_log)
            if self.user == None:
                self.show_alert_dialog("El email o la contraseña no coinciden")
                self.clear_login()
            else:
                self.screen_manager.transition.direction = "left"

                if self.user["account_type_id"] == 1:
                    self.load_main_menu_user()
                    self.screen_manager.current = "Inicio"
                    self.clear_login()
                    print(self.user)
                else:
                    self.load_main_menu_tutors()
                    self.screen_manager.current = "InicioTutor"
                    self.clear_login()

    # Tutorship
    def load_new_tutorship_menu(self):
        self.screen_manager.add_widget(Builder.load_file("style/agendarTutoria.kv"))
        career_id = func.get_career_by_user_id(self.user["user_id"])
        dpdown_subject_items = [
            {
                "viewclass": "IconListItem",
                "icon": "bookshelf",
                "text": f"{(i[0])} {i[1]}",
                "height": dp(56),
                "on_release": lambda x=f"{i[0]} {i[1]}": self.set_item_subject(x),
            }
            for i in func.get_subjects_by_career_id(career_id[0])
        ]

        self.menu_subject = MDDropdownMenu(
            caller=self.screen_manager.get_screen("agendarTutoria").ids.asignatura,
            width_mult=8,
            ver_growth="up",
            hor_growth="right",
            items=dpdown_subject_items,
        )

        self.menu_subject.bind()

    def load_main_menu_user(self):
        self.screen_manager.add_widget(Builder.load_file("style/Inicio.kv"))
        self.screen_manager.get_screen(
            "Inicio"
        ).ids.lbBienvenida.text = f"{self.user['name']}"
        self.load_new_tutorship_menu()

    def set_item_subject(self, text_item):
        self.screen_manager.get_screen("agendarTutoria").ids.asignatura.text = text_item
        self.subject_id = re.findall("\d+", text_item)[0]
        tutors = func.get_tutor_by_subject_id(self.subject_id)

        dpdown_tutors_items = [
            {
                "viewclass": "IconListItem",
                "icon": "account",
                "text": f"{tutor['name']}",
                "height": dp(56),
                "on_release": lambda x=tutor: self.set_item_tutors(x, self.subject_id),
            }
            for tutor in tutors
        ]
        self.menu_tutor = MDDropdownMenu(
            caller=self.screen_manager.get_screen("agendarTutoria").ids.tutor,
            ver_growth="up",
            hor_growth="right",
            items=dpdown_tutors_items,
            width_mult=8,
        )
        self.menu_tutor.bind()
        self.screen_manager.get_screen("agendarTutoria").ids.tutor.pos = (60, 500)
        self.menu_subject.dismiss()

    def set_item_tutors(self, tutor, subject_id):
        self.tutor = tutor
        self.screen_manager.get_screen("agendarTutoria").ids.tutor.text = self.tutor[
            "name"
        ]
        self.screen_manager.get_screen("agendarTutoria").ids.schedule.pos = (60, 400)

        self.schedule = func.get_schedule_by_subject_and_tutor(
            subject_id, tutor["user_id"]
        )

        dpdown_schedule_items = [
            {
                "viewclass": "IconListItem",
                "icon": "clock-outline",
                "text": f"{spot['day']} {spot['init_time']} {spot['end_time']}",
                "height": dp(56),
                "on_release": lambda x=spot: self.set_item_schedule(x),
            }
            for spot in self.schedule
        ]

        self.menu_schedule = MDDropdownMenu(
            caller=self.screen_manager.get_screen("agendarTutoria").ids.schedule,
            ver_growth="up",
            hor_growth="right",
            items=dpdown_schedule_items,
            width_mult=8,
        )
        self.menu_schedule.bind()
        self.menu_tutor.dismiss()

    def set_item_schedule(self, spot):
        self.screen_manager.get_screen(
            "agendarTutoria"
        ).ids.schedule.text = f"{spot['day']} {spot['init_time']} {spot['end_time']}"
        self.selected_spot = spot
        dpdown_aula_items = [
            {
                "viewclass": "IconListItem",
                "icon": "town-hall",
                "text": f"{i[1]}",
                "height": dp(56),
                "on_release": lambda x=i: self.set_item_aula(x),
            }
            for i in func.get_table(7)
        ]

        self.menu_aula = MDDropdownMenu(
            caller=self.screen_manager.get_screen("agendarTutoria").ids.aula,
            ver_growth="up",
            hor_growth="right",
            items=dpdown_aula_items,
            width_mult=8,
        )
        self.menu_aula.bind()
        self.screen_manager.get_screen("agendarTutoria").ids.aula.pos = (60, 300)
        self.menu_schedule.dismiss()

    def set_item_aula(self, aula):
        self.aula = aula
        self.screen_manager.get_screen("agendarTutoria").ids.aula.text = self.aula[1]
        self.menu_aula.dismiss()

    def clear_new_tutorship(self):
        self.screen_manager.get_screen("agendarTutoria").ids.asignatura.text = ""
        self.screen_manager.get_screen("agendarTutoria").ids.tutor.pos = (-6000, 500)
        self.screen_manager.get_screen("agendarTutoria").ids.tutor.text = ""
        self.screen_manager.get_screen("agendarTutoria").ids.schedule.pos = (-6000, 500)
        self.screen_manager.get_screen("agendarTutoria").ids.schedule.text = ""
        self.screen_manager.get_screen("agendarTutoria").ids.aula.pos = (-6000, 500)
        self.screen_manager.get_screen("agendarTutoria").ids.aula.text = ""

    def load_summary(self, id):
        self.screen_manager.add_widget(Builder.load_file("style/summary.kv"))
        data_tutorship = func.get_tutorship(id)
        schedule = func.get_schedule_by_id(data_tutorship["schedule_id"])
        subject = func.get_subject_by_id(data_tutorship["subject_id"])
        classroom = func.get_classroom_by_id(data_tutorship["classroom_id"])
        tutor = func.get_user_by_id(data_tutorship["tutor_id"])
        self.user_id_del = id
        self.screen_manager.get_screen("summary").add_widget(
            MD3Card(
                line_color=(0.2, 0.2, 0.2, 0.8),
                style="filled",
                md_bg_color="#FFFBEA",
                pos_hint={"center_x": 0.50, "center_y": 0.50},
                text=f"""
            Materia: {subject['name']}
            Salon: {classroom['classroom_name']}
            Horario: {schedule['day']} {schedule['init_time']} - {schedule['end_time']}
            Tutor: {tutor['name']}
            """,
            )
        )

    def delete_summary(self):
        self.delete_tutorship()
        self.screen_manager.transition.direction = "left"
        self.screen_manager.current = "Inicio"

    def delete_tutor(self):
        self.delete_tutorship()
        self.screen_manager.transition.direction = "left"
        self.screen_manager.current = "InicioTutor"

    def delete_tutorship(self):
        print("ola", self.user_id_del)
        func.delete_by_id(5, self.user_id_del)

    def create_tutorship(self):
        a = self.selected_spot["schedule_id"]
        b = self.subject_id
        c = self.aula[0]
        d = self.tutor["user_id"]
        e = self.user["user_id"]
        func.new_tutorship(a, b, c, d, e)
        last_tutorship = func.get_last_tutorship()
        self.summary_id = last_tutorship["tutorship_id"]
        self.clear_new_tutorship()
        self.load_summary(self.summary_id)
        self.screen_manager.transition.direction = "left"
        self.screen_manager.current = "summary"

    # Menu Tutores
    def load_main_menu_tutors(self):
        self.screen_manager.add_widget(Builder.load_file("style/inicioTutor.kv"))
        tutorships_by_tutor = func.get_tutorship_by_tutor_id(self.user["user_id"])
        box = self.screen_manager.get_screen("InicioTutor").ids.box
        for tutorship in list(tutorships_by_tutor):
            schedule = func.get_schedule_by_id(tutorship["schedule_id"])
            subject = func.get_subject_by_id(tutorship["subject_id"])
            classroom = func.get_classroom_by_id(tutorship["classroom_id"])
            student = func.get_user_by_id(tutorship["student_id"])
            self.user_id_del = tutorship["tutorship_id"]
            box.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style="filled",
                    md_bg_color="#FFFBEA",
                    text=f"""
                Codigo: {tutorship["tutorship_id"]}
                Materia: {subject['name']}
                Salon: {classroom['classroom_name']}
                Horario: {schedule['day']} {schedule['init_time']} - {schedule['end_time']}
                Estudiante: {student['name']}
                """,
                )
            )


if __name__ == "__main__":
    LabelBase.register(name="zapf", fn_regular="fonts/zapf.ttf")
    LabelBase.register(name="galliard", fn_regular="fonts/galliard-bt-bold.ttf")
    GUI().run()
