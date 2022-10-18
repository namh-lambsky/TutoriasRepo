class tutorship:
    def __init__(self,id_tutorship,student_email,id_subject,id_classroom):
        self.id_tutorship=id_tutorship
        self.student_email=student_email
        self.id_subject=id_subject
        self.id_classroom=id_classroom

    def get_id_tutorship(self):
        return self.id_tutorship

    def get_student_email(self):
        return self.student_email

    def get_id_subject(self):
        return self.id_subject

    def get_id_classroom(self):
        return self.id_classroom