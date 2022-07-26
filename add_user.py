from data_manager import DataManager


class AddUser:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None

    def get_user_data(self):
        self.first_name = input("Enter your first name:  ")
        self.last_name = input("Enter your last name:  ")
        self.email_validation()

    def email_validation(self):
        email1 = input("Enter your email:  ").strip().lower()
        email2 = input("Enter your email again:  ").strip().lower()

        if email1 != email2:
            return self.email_validation()
        else:
            self.email = email1

    def add_user(self):
        self.get_user_data()
        user_data = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }
        DataManager().add_data(sheet_name="users", data=user_data)
