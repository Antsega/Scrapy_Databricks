## Databricks Workbook: Segarra Web Scraper
This workbook houses a BeautifulSoup scraper configured to extract pertinent data from "https://segarratech.com" and subsequently saves the collated data to the Databricks File System (DBFS). The data is then read into a PySpark DataFrame for further processing.



---
## Table of Contents
1. [Installation](#installation)
2. [Usage](#Usage)
3. [Code Structure](#Code-Structure)
4. [Features](#Features)
5. [Version Control](#Version-Control)

---
_Installation_ <a name="installation"></a>
The notebook is designed to be run on Databricks. All you need to do is import the notebook into your Databricks workspace.

---
_Usage_ <a name="usage"></a>
Run the notebook: The whole notebook can be run in one go. It will execute the Segarra web scraper and generate a JSON file in DBFS housing the scraped data. The notebook will then read this data into a DataFrame.
Check the output: Post the run, you can verify the scraped data by viewing the DataFrame created by the notebook.

---
_Code Structure_ <a name="code-structure"></a>
The workbook is divided into distinct cells.

Cell 1: This cell includes the core scraping logic using BeautifulSoup. It extracts specific data from the target webpage and saves it as a JSON file in the DBFS.

Cell 2: Lists all contents of the directory "/tmp/test-folder" in the DBFS.

Cell 3: It reads the JSON file (containing scraped data) into a DataFrame and displays the same.


---
_Features_ <a name="features"></a>
- BeautifulSoup Scraper: The scraper navigates through "https://segarratech.com", gleans specific details, transforms this data into a JSON format, and saves the result as a JSON file in DBFS.
- PySpark: The stored JSON data in DBFS is read into a PySpark DataFrame for subsequent processing.

---
_Version Control <a name="version-control"></a>
As of now, the notebook does not contain any version control system. The user is advised to manually maintain different versions of the notebook for tracking purposes.

## Current solution
After facing challenges with the previous Scrapy implementation, the notebook has been revised to use BeautifulSoup for the web scraping task. This tool works more harmoniously in the notebook environment and can be run multiple times within the same session without issues. All web scraping operations are now contained within a single cell. Post scraping, the data is saved to DBFS as a JSON file and then read into a DataFrame.
