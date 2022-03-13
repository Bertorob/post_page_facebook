import os, random
import requests
import shutil

page_id = "your page id"
token = "YOUR TOKEN"
link =  f"https://graph.facebook.com//v13.0/{page_id}/photos"

def main():
    image = random.choice(os.listdir("input"))
    myobj = {
        'caption': "your image caption",
        'access_token': token
    }
    files={"src": open("input/" + image, 'rb')}

    x = requests.post(link, data = myobj, files=files)

    print(x.text)

    shutil.move("input/" + image, "published/" )

if __name__ == "__main__":
    main()