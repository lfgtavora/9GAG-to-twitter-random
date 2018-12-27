from selenium import webdriver
import xml.etree.ElementTree as ET
import re
import html.parser as htmlparser
from sqlite import insertdb
from post import upload_on_twitter

url = 'http://9gagrss.com/feed/'

# #setup chrome
chrome_path = r"chromedrive/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.get(url)

root = ET.fromstring(driver.page_source)


def extract_url(text):
    src = re.search('(?<=src=").*?(?=")', text)
    return src[0]


def post_type(link):
    if link.endswith('.mp4'):
        return 'video'
    else:
        return 'image'


if __name__ == '__main__':
    # scrap last 30 top post on 9GAG home and insert in database
    for item in root.iter('item'):
        title = htmlparser.unescape(item[0].text)  # encoding utf-8
        link = extract_url(item[1].text)
        type = post_type(link)

        insertdb(title, link, type)

        print(title)
        print(link)

    # Get random post in database and publish on twitter
    upload_on_twitter()
    print('UPLOAD SUCCESSFUL!')
