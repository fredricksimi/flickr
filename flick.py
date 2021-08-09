import requests
import json

new_list = []
our_data = requests.get('https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=9037de3cf6ce2eba6fbd558071f76bef&text=face&format=json&nojsoncallback=1')

our_json_data = our_data.json()

for data in our_json_data['photos']['photo']:

    new_structure = {
        "id":data['id'],
        "owner":data['owner'],
        "image_url":f"https://flickr.com/photos/{data['owner']}/{data['id']}",
        "title":data['title'],
    }
    new_json = json.dumps(new_structure)
    our_file = open('ourdata.json', 'a')
    our_file.write(f"{new_json}\n")
    new_list.append(new_json)

our_file.close()

