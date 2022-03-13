import os, random
import requests
import shutil
import json

from src.lib.io import read_config

def main():   

    config = read_config()
    endpoint = f"https://graph.facebook.com//v13.0/{config['page_id']}/photos"

    image = random.choice(os.listdir("input"))
    myobj = {
        'caption': config["post_caption"],
        'access_token': config["access_token"]
    }
    files={"src": open("input/" + image, 'rb')}

    x = requests.post(endpoint, data = myobj, files=files)

    print(x.text)

    shutil.move("input/" + image, "published/" )

if __name__ == "__main__":
    main()