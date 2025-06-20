from google.cloud import storage
import os

# Set the credentials programmatically
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\DELL\Desktop\Data Analytics GUI\GCP\zero-workers-dde9e6f467ca.json"

# Initialize the client
client = storage.Client()

# List all buckets
buckets = list(client.list_buckets())
for bucket in buckets:
    print(bucket.name)
