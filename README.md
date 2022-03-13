# post_page_facebook
Automatic facebook post for pages.

# Getting started
1. Put your collection of images in the `input` dir.
2. Fill in the `etc/config.yml` with your access token, your page id and the caption for your posts.
3. Run the script every time you want to publish a picture on your page with `python main.py`.

The script will choose a random picture from the `input` dir and move it to the `published` dir.
