from users.User import User


class FreeUser(User):
    def __init__(self, name, email, license) -> None:
        super().__init__(name, email, license)

    @property
    def get_posts(self):
        return self._posts

    @get_posts.setter
    def add_post(self, post):
        if len(self._posts) + 1 > 2:
            return "Upgrade to a Premium account to enable more blog posts"
        else:
            self._posts.append(post)
