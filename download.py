import argparse
import os


try:
	import scrapy
except ImportError:
	print("Please install the scrapy package")
	print("Run the following command: pip install scrapy")
	exit()

import scrapy
from scrapy.crawler import CrawlerProcess
from das.spiders.video import VideoSpider




currentDir = os.path.dirname(os.path.realpath(__file__))



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument( "-o", "--outputFolder", help="The place where the DAS videos will be stored")
	args = parser.parse_args()


	if args.outputFolder:
		outputFolder =  os.path.join(currentDir, args.outputFolder)
	else:
		outputFolder = os.path.join(currentDir, 'videos')

	if not os.path.exists(outputFolder):
		os.makedirs(outputFolder)

	process = CrawlerProcess()
	process.crawl(VideoSpider, outputFolder)
	process.start() # the script will block here until the crawling is finished


