from users.User import User

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        user = User(name)
        self.users.append(user)
        print(f"Utilisateur ajouté : {user}")

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None
