class Tutorship:
    def __init__(self,schedule_id,subject_id,classroom_id,tutor_id,student_id):
        self.schedule_id=schedule_id
        self.subject_id=subject_id
        self.classroom_id=classroom_id
        self.tutor_id=tutor_id
        self.student_id=student_id

    def get_schedule_id(self):
        return self.schedule_id

    def get_subject_id(self):
        return self.subject_id

    def get_classroom_id(self):
        return self.classroom_id

    def get_tutor_id(self):
        return self.tutor_id

    def get_student_id(self):
        return self.student_id