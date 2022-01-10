from instabot import Bot


class InstaBot():
    def __init__(self, username, password) -> None:
        self.bot = Bot(unfollow_delay=10)
        self.bot_uname = username
        self.bot_pass = password
        self.bot.login(username=self.bot_uname,
                       password=self.bot_pass, is_threaded=True)

    def bot_logout(self):
        self.bot.logout()

    def get_mean_people(self):  # accounts that don't follow back
        followers = set(self.bot.get_user_followers(
            self.bot.user_id))
        following = set(self.bot.get_user_following(
            self.bot.user_id))
        return (followers, following, following-followers)

    def get_mean_id_name(self):
        ids = list(self.get_mean_people()[2])
        id_name = []

        for i in ids:
            uname_of_id = self.bot.get_username_from_user_id(i)
            id_name.append((i,
                            uname_of_id,
                            'Private' if (self.bot.get_user_info(i)[
                                          "is_private"]) else 'Public',
                            self.bot.get_user_info(i)
                            ['hd_profile_pic_url_info']['url']
                            ))
        return id_name

    def unfollow_single(self, uname):
        self.bot.unfollow(uname)

    def unfollow_many(self, uname_list):
        self.bot.unfollow_users(uname_list)
