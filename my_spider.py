import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json
from datetime import datetime
from pyspark.sql import SparkSession
from multiprocessing import Process


class TestSpider(scrapy.Spider):

    name = "segarra"
    start_urls = ["https://segarratech.com"]

    def parse(self, response):
        text = []
        text.append ({
            "web-title" : response.xpath('//title/text()').get(),
            "top" : response.css('h1.title::text').get(),
            "List Header" : response.css('h2.task-list-title::text').get(),
            "Button" : response.css('button.btn.create::text').get(),
            "Test" : "Test",
            "Test" : "Test2",
            "Test" : "Test3"
        })

        # Unique file name with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # dbfs_path = f"/tmp/test-folder/text_{timestamp}.json"
        dbfs_path = f"/tmp/test-folder/test1.json"
        
        # Convert text list to json lines
        json_lines = ""
        for line in text:
            json_lines += json.dumps(line) + '\n'
        
        # Save to dbfs
        dbutils.fs.put(dbfs_path, json_lines, overwrite=True)

# Define the function that will start our spider
def run_spider(spider):
    process = CrawlerProcess(settings={
        "LOG_LEVEL": "CRITICAL",
    })
    process.crawl(spider)
    process.start()

# Create a new process and start it
p = Process(target=run_spider, args=(TestSpider,))
p.start()

# Wait for the process to finish
p.join()
