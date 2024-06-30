import boto3


# Create a aws client to connecto to s3
# https://www.learnatnoon.com/s/en-pk2/what-is-the-difference-between-client-and-server-in-computer-science
client = boto3.client('s3')

# Get a list of buckets in s3
# Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_buckets.html
response = client.list_buckets()

# Loop through each bucket
# Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/object/get.html
# get(val1 if it exists, val2 if it does not)
for b in response.get("Buckets", None):
    print(b.get("Name", None))

# boto3 closes automatically by itself!