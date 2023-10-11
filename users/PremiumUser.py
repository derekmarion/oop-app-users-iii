from users.User import User


class PremiumUser(User):
    def __init__(self, name, email, license) -> None:
        super().__init__(name, email, license)