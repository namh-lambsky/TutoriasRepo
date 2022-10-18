class Student:
    def __init__(self,rating,career_id,student_id):
        self.rating=rating
        self.career_id=career_id
        self.student_id=student_id

    def get_rating(self):
        return self.rating

    def get_career_id(self):
        return self.career_id

    def get_student_id(self):
        return self.student_id

