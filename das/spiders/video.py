import scrapy

from subprocess import call

BASE_PATH = "/media/greg/Data/DestroyAllSoftware/scripts/das/videos/"

class VideoSpider(scrapy.Spider):
    name = 'video'

    start_urls = ['https://www.destroyallsoftware.com/screencasts/catalog']

    def parse(self, response):
        # Find links to each dentist page
        videoPages = response.xpath("//a[contains(@href, 'screencasts/catalog/')]/@href").extract()
        for videoPage in videoPages:
            yield response.follow(videoPage, self.parseVideoPage)

    def parseVideoPage(self, response):
        VIDEO_URL_START = 'https://destroyallsoftware.s3.amazonaws.com/'
        # First link is 4k, which I don't want
        urlStart = response.text.find(VIDEO_URL_START) 
        # Second link is 1080p, which we want
        urlStart = response.text.find(VIDEO_URL_START, urlStart + 1) 
        urlEnd = response.text.find('"', urlStart)
        url = response.text[urlStart:urlEnd]
        url = url.replace('-4k.mp4', '-1080p.mp4', 1)

        URLStart = "https://destroyallsoftware.s3.amazonaws.com/"
        filenameStart = url.find(URLStart) + len(URLStart)
        filenameEnd = url.find("?", filenameStart)
        filename = url[filenameStart:filenameEnd]

        
        command = 'wget -c -O "%s%s" "%s"' % (BASE_PATH, filename, url)
        PATH = "/media/greg/Data/DestroyAllSoftware/scripts/das/videos/"
        call(["wget", "-c", "-O", PATH + filename, url])
        




