import os
import requests
from zipfile import ZipFile

# Dataset URLs (replace with actual URLs)
dataset_urls = {
    "FinQA": "http://example.com/finqa.zip",
    "TAT-QA": "http://example.com/tatqa.zip",
    "TheoremQA": "http://example.com/theoremqa.zip",
    "BizBench": "http://example.com/bizbench.zip",
    "FinanceMATH": "http://example.com/financemath.zip"
}

# Directory to save datasets
data_dir = "data/"

# Function to download and unzip datasets
def download_and_extract(dataset_name, url):
    print(f"Downloading {dataset_name}...")
    response = requests.get(url)
    zip_path = os.path.join(data_dir, f"{dataset_name}.zip")
    
    with open(zip_path, 'wb') as f:
        f.write(response.content)

    print(f"Extracting {dataset_name}...")
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(data_dir, dataset_name))
    
    print(f"{dataset_name} downloaded and extracted successfully!")

# Main function
def main():
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    for dataset_name, url in dataset_urls.items():
        download_and_extract(dataset_name, url)

if __name__ == "__main__":
    main()
