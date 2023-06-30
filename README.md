## Databricks Workbook: Segarra Web Scraper
This workbook houses a Scrapy spider configured to extract pertinent data from "https://segarratech.com" and subsequently saves the collated data to the Databricks File System (DBFS). The data is then read into a PySpark DataFrame for further processing.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#Usage)
3. [Code Structure](#Code-Structure)
4. [Features](#Features)
5. [Version Control](#Version-Control)

_Installation_ <a name="installation"></a>
The notebook is designed to be run on Databricks. All you need to do is import the notebook into your Databricks workspace.
---
_Usage_ <a name="usage"></a>
Run the notebook: The whole notebook can be run in one go. It will execute the Segarra web scraper and generate a JSON file in DBFS housing the scraped data. The notebook will then read this data into a DataFrame.
Check the output: Post the run, you can verify the scraped data by viewing the DataFrame created by the notebook.
---
_Code Structure_ <a name="code-structure"></a>
The workbook is divided into distinct cells.

Cell 1: This cell includes the core scraping logic within the TestSpider class, which is a Scrapy spider. It extracts specific data from the target webpage.

Cell 2: It's responsible for triggering a Scrapy CrawlerProcess and initiating the TestSpider.

Cell 3: Lists all contents of the directory "/tmp/test-folder" in the DBFS.

Cell 4: It reads the JSON file (containing scraped data) into a DataFrame and displays the same.

Cell 5: This cell initializes a new git repository for version control.

---
_Features_ <a name="features"></a>
- Scrapy Spider: The spider, named 'Segarra', navigates through "https://segarratech.com", gleans specific details, transforms this data into a JSON format, and saves the result as a JSON file in DBFS.
- PySpark: The stored JSON data in DBFS is read into a PySpark DataFrame for subsequent processing.
- Git: The notebook initiates a new git repository to enable version control.