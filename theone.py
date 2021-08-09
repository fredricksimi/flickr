from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys
import json


key = "9037de3cf6ce2eba6fbd558071f76bef"
secret = "543c6db6d420ed53"
wait_time = 1

keyname = 'face'
savedir = "./Faces"


flickr = FlickrAPI(key, secret, format='parsed-json')


result  = flickr.photos.search(
    text = keyname,
    per_page = 100,
    media = 'photos',
    sort = 'relevance',
    safe_seach = 1,
    extras = 'url_q, licence'
)

photos = result['photos']

our_json_data = photos['photo']

for data in our_json_data:

    new_structure = {
        "id":data['id'],
        "owner":data['owner'],
        "image_url":f"{data['url_q']}",
        "title":data['title'],
    }
    new_json = json.dumps(new_structure)
    our_file = open('2-ourdata.json', 'a')
    our_file.write(f"{new_json}\n")

our_file.close()


for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)