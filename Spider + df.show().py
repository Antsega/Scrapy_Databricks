# Databricks notebook source
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Define the URL
url = "https://segarratech.com"

# Send the GET request
response = requests.get(url)

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements
web_title = soup.find('title').text
top = soup.find('h1', {'class': 'title'}).text
list_header = soup.find('h2', {'class': 'task-list-title'}).text
button = soup.find('button', {'class': 'btn create'}).text

# Prepare the data dictionary
data = {
    "web-title" : web_title,
    "top" : top,
    "List Header" : list_header,
    "Button" : button,
    "Test" : "SoupTest",
}

# Unique file name with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
dbfs_path = f"/tmp/crawl_{timestamp}.json"

# Convert data dict to json
json_data = json.dumps(data)

# Save to dbfs
dbutils.fs.put(dbfs_path, json_data, overwrite=True)


# COMMAND ----------

dbutils.fs.ls ("/tmp/")

# COMMAND ----------

# Grab your desired name value from your dir
f = "/tmp/crawl_2023-06-30_21-10-37.json"
df = spark.read.json(f)
df.show()

# COMMAND ----------


