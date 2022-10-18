class subject:
    def __init__(self,subject_id,name,career_id):
        self.id_subject=subject_id
        self.name=name
        self.career_id=career_id

    def get_subject_id(self):
        return self.id_subject

    def get_name(self):
        return self.name

    def get_career_id(self):
        return self.career_id
