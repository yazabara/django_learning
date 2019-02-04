from workout_portal.models import SimpleUser


class SimpleUserBuilder(object):

    def __init__(self, profile_url="profile_url", username="username", password="password", telephone=12345678901,
                 profile_img="/images/img.png"):
        self.profile_url = profile_url
        self.username = username
        self.password = password
        self.telephone = telephone
        self.profile_img = profile_img

    def build(self):
        return SimpleUser(profile_url=self.profile_url, username=self.username, password=self.password,
                          telephone=self.telephone, profile_img=self.profile_img)
