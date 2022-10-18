class User:
    def __init__(self,user_id,email,password,name,account_type_id):
        self.user_id=user_id
        self.email=email
        self.password=password
        self.name=name
        self.account_type_id=account_type_id

    def get_user_id(self):
        return self.user_id

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_name(self):
        return self.name

    def get_account_type_id(self):
        return self.account_type_id