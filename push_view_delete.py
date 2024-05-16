import boto3


# open client
client = boto3.client('s3')

# some initial variables
bucket_name = "tkh-nyc-intrusions"

# open the file in binary format, and save into the var 'data'
# Documentation: https://book.pythontips.com/en/latest/context_managers.html
with open("example.txt", "rb") as f:
    data = f.read()

### ADDING OBJECTS TO A BUCKET ###
# Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object.html
response = client.put_object(
    Body=data,
    Bucket=bucket_name,
    Key="tux-image"
)

print("Result of pushing object", response)

### GETTING OBJECTS FROM A BUCKET ###
# Get the list of objects in s3
response = client.list_objects(
    Bucket=bucket_name
)
print("objects currently in Bucket:")
# iterate over names
for i in response.get("Contents", None):
    print(i.get("Key", None))

### DELETING OBJECTS FROM A BUCKET ###
# response = client.delete_object(
#     Bucket=bucket_name,
#     Key="tux-image"
# )

#print("Result of deleting object", response)