from ARS.models.admin import Admin

class AdminService:

    def __init__(self):
        self.admin_list = []

    def add_admin(self):
        aid = input("Enter Admin ID: ")

        for a in self.admin_list:
            if a.aid == aid:
                print("Admin already exists.")
                return

        name = input("Enter Name: ")

        admin = Admin(aid, name)
        self.admin_list.append(admin)

        print("Admin Added Successfully.")

    def view_admins(self):
        for a in self.admin_list:
            print(a.aid, a.name)