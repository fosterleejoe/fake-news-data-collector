
class FakenewsUtils:
    def split_news_twitter_url(self,url):
        url = url.replace("https://twitter.com/", "")
        url = url.split("/")
        user = None
        status = None
        if len(url) == 3:
            user = url[0]
            status = url[2]

        return user, status
