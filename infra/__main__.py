"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('ammoseekr-ammo-listings', location="US")

# Export the DNS name of the bucket
pulumi.export('ammo_listings', bucket.url)
