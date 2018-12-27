from sqlite import getpost
import urllib.request
from twython import Twython

APP_KEY = '****'
APP_SECRET = '****'
OAUTH_TOKEN = '****'
OAUTH_TOKEN_SECRET = '****'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


def download_file(url, post_type):
        if post_type == 'video':
            extension = '.mp4'
        else:
            extension = '.jpg'

        urllib.request.urlretrieve(url, "temp/temp" + extension)


def upload_video(title):
    video = open('temp/temp.mp4', 'rb')
    response = twitter.upload_video(media=video, media_type='video/mp4', media_category='tweet_video', check_progress=True)
    twitter.update_status(status=title, media_ids=[response['media_id']])


def upload_image(title):
    photo = open('temp/temp.jpg', 'rb')
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=title, media_ids=[response['media_id']])


def upload_on_twitter():
    title, link, post_type = getpost()

    # download url to temp folder
    download_file(link, post_type)

    if post_type == 'video':
        upload_video(title)
    else:
        upload_image(title)

