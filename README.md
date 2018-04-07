# Destroy All Software Downloader
A simple script to download all the [Destroy All Software screencasts](https://www.destroyallsoftware.com/screencasts/catalog) during the week they're free. 

If you like DAS, consider subscribing!

To run it, execute the following line which will download the videos in the *videos* directory:

`python3 download.py`

If you want to choose the output folder, run it like this:

`python3 download.py -o myVideos`

Requirements:
- Python 3
- Scrapy (scraper packager; the script will tell you if you don't have it and how to install it)
- Wget (to download the videos)

