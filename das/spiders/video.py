import scrapy
import os
from subprocess import call

class VideoSpider(scrapy.Spider):
    name = 'video'

    start_urls = ['https://www.destroyallsoftware.com/screencasts/catalog']

    def __init__(self, outputFolder):
        self.outputFolder = outputFolder

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

        
        command = 'wget -c -O "%s" "%s"' % (os.path.join(self.outputFolder, filename), url)
        print(command)
        call(["wget", "-c", "-O", os.path.join(self.outputFolder, filename), url])
        




