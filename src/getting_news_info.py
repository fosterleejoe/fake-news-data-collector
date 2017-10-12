import pandas as pd
import twitter

api = twitter.Api(consumer_key="AiqPyiPhKeEHg",
                  consumer_secret="OWfcdd3HrZFA7lxVlsEhNF4k6TRhJo9qAzc",
                  access_token_key="263395ddd5qRuwhXWbZA9WQIhz3qRw7kXYsuVC",
                  access_token_secret="Kc9BGOGd2eAyPUywnOcwfqMyhvT")

def split_news_url(url):
    url = url.replace("https://twitter.com/","")
    url = url.split("/")
    if len(url) == 3:
        user = url[0]
        status = url[2]
        print ("\nusuario: " + user)
        print ("\nstatus: " + status)
        return user, status


def get_df_status(url):
    user, status = split_news_url(url)
    user_timeline = api.GetUserTimeline(screen_name='@' + user)
    user_info = api.GetUser(screen_name='@' + user)
    try:
        default_profile_image = user_info.AsDict()['default_profile_image']
    except:
        default_profile_image = False

    try:
        default_profile = user_info.AsDict()['default_profile']
    except:
        default_profile = False

    df = pd.DataFrame(
    { status :
        [
          status,
          user,
          user_info.AsDict()['created_at'],
          user_info.AsDict()['screen_name'],
          user_info.AsDict()['statuses_count'],
          default_profile,
          default_profile_image,
          user_info.AsDict()['favourites_count'],
          user_info.AsDict()['friends_count'],
          user_info.AsDict()['id'],
          user_info.AsDict()['lang'],
          user_info.AsDict()['name'],
          user_info.AsDict()['profile_background_color'],
          user_info.AsDict()['profile_image_url']
      ]
    },
    index=['status','user','created_at','screen_name','statuses_count','default_profile','default_profile_image','favourites_count','friends_count','id','lang','name','profile_background_color','profile_image_url']
    )
    dft = df.transpose()
    return dft


df1 = get_df_status("https://twitter.com/Beatriz49411812/status/910571458719473664")
df1 = df1.append(get_df_status("https://twitter.com/ERANDISHADEMORE/status/910568963649634305"))
df1 = df1.append(get_df_status("https://twitter.com/FeysPerson/status/910344589990617088"))
df1 = df1.append(get_df_status("https://twitter.com/dracas_llodi/status/910341085372837888"))
df1 = df1.append(get_df_status("https://twitter.com/mtz382/status/910337544897880064"))
df1 = df1.append(get_df_status("https://twitter.com/atristainted/status/914178687183892482"))
df1 = df1.append(get_df_status("https://twitter.com/trespacos/status/914554291528044544"))

print df1
print ("fin")
