# Databricks notebook source
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json
from datetime import datetime
from pyspark.sql import SparkSession


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
            "Test" : "Test2"
        })

        # Unique file name with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        dbfs_path = f"/tmp/test-folder/text_{timestamp}.json"
        
        # Convert text list to json lines
        json_lines = ""
        for line in text:
            json_lines += json.dumps(line) + '\n'
        
        # Save to dbfs
        dbutils.fs.put(dbfs_path, json_lines, overwrite=True)

# Instantiate a CrawlerProcess
process = CrawlerProcess(settings={
    "LOG_LEVEL":"CRITICAL",
})

# Start the spider
process.crawl(TestSpider)
process.start()  # the script will block here until the crawling is finished


# COMMAND ----------

dbutils.fs.ls ("/tmp/test-folder")

# COMMAND ----------

f = "/tmp/test-folder/text_2023-06-27_20-32-20.json"
df = spark.read.json(f)
df.show()

# COMMAND ----------

git init

# COMMAND ----------


