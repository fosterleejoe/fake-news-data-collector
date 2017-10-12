import twitter
import pandas as pd
from fakenews.utils.fakenewsUtils import *


class TwitterService:
    def __init__(self, cfg):
        '''

        :param cfg:
        '''
        self.cfg = cfg
        self.twitter = twitter.Api(
            consumer_key=cfg['consumer_key'],
            consumer_secret=cfg['consumer_secret'],
            access_token_key=cfg['access_token_key'],
            access_token_secret=cfg['access_token_secret']
        )
        self.fakenewsUtils = FakenewsUtils()


    def get_user_df(self, user):
        '''

        :param url:
        :return:
        '''
        user_timeline = self.twitter.GetUserTimeline(screen_name='@' + user)
        user_info = self.twitter.GetUser(screen_name='@' + user)
        user_info = user_info.AsDict()
        try:
            default_profile_image =
        except:
            default_profile_image = False

        try:
            default_profile =
        except:
            default_profile = False

        df = pd.DataFrame(
            {
            user : [
                user,
                self.get_value_from_dict(user_info, 'created_at'),
                self.get_value_from_dict(user_info, 'created_at'),
                self.get_value_from_dict(user_info, 'screen_name'),
                self.get_value_from_dict(user_info, 'statuses_count'),
                self.get_value_from_dict(user_info, 'default_profile_image'),
                self.get_value_from_dict(user_info, 'default_profile'),
                self.get_value_from_dict(user_info, 'favourites_count'),
                self.get_value_from_dict(user_info, 'friends_count'),
                self.get_value_from_dict(user_info, 'id'),
                self.get_value_from_dict(user_info, 'lang'),
                self.get_value_from_dict(user_info, 'name'),
                self.get_value_from_dict(user_info, 'profile_background_color'),
                self.get_value_from_dict(user_info, 'profile_image_url')
                ]
            },
            index=['status',  'user', 'created_at', 'screen_name', 'statuses_count', 'default_profile',
                   'default_profile_image', 'favourites_count', 'friends_count', 'id', 'lang', 'name',
                   'profile_background_color', 'profile_image_url']
        )
        dft = df.transpose()
        return dft

    def get_status_df(self,status):
        '''

        :param status:
        :return:
        '''
        status_info = self.twitter.GetStatus(status)

        df = pd.DataFrame({})
        return df

    def get_value_from_dict(self,dict,value):
        try:
            return dict[value]
        except:
            return None
