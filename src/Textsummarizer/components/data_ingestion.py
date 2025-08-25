import os
import urllib.request as request
import zipfile
from Textsummarizer.logging import logger
from Textsummarizer.utils.common import get_size
from Textsummarizer.entity import DataIngestionConfig
from pathlib import Path
import os
import ssl
import certifi
import urllib.request




class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self):
        url = self.config.source_URL
        local_path = self.config.local_data_file

        # Create SSL context using certifi
        ssl_context = ssl.create_default_context(cafile=certifi.where())

        # Download the file securely
        with urllib.request.urlopen(url, context=ssl_context) as response:
            with open(local_path, 'wb') as out_file:
                out_file.write(response.read())

        print(f"✅ File downloaded successfully to {local_path}")

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)