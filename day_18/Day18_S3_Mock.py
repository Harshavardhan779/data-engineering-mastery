import os
import shutil
from datetime import datetime

# 1. The Setup: Define our "Local Stage" and "Cloud Bucket"
LOCAL_SOURCE = "scripts/"  # Where our code/data is currently
CLOUD_BUCKET = "mock_s3_bucket" # This acts as our AWS S3

def upload_to_s3(file_name):
    # Check if file exists locally
    if not os.path.exists(file_name):
        print(f"⚠️ File {file_name} not found locally.")
        return

    # 2. Partitioning: Create a path based on DATE (Standard Data Eng practice)
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Target Key: s3://bucket/2025-12-26/filename
    s3_key = os.path.join(CLOUD_BUCKET, today)
    
    # Ensure "Cloud" folder exists
    os.makedirs(s3_key, exist_ok=True)
    
    # 3. The Upload: Copy the file
    destination = os.path.join(s3_key, file_name)
    shutil.copy(file_name, destination)
    
    print(f"☁️ Uploaded: {file_name} -> {destination}")

# Let's upload the files we created in previous days
files_to_upload = ["api_users.csv", "scraped_products.csv"]

print("🚀 Starting Cloud Upload Job...")
for file in files_to_upload:
    # (Creating dummy files if they don't exist, just for this test)
    if not os.path.exists(file):
        with open(file, 'w') as f: f.write("dummy data")
        
    upload_to_s3(file)

print("\n✅ Cloud Sync Complete. Check the 'mock_s3_bucket' folder.")