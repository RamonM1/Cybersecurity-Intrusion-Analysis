import boto3
import pandas as pd
import io

# some initial variables
bucket_name = "tkh-nyc-intrusions"
object_key = 'tux-image'

# open client
client = boto3.client('s3')

### DOWNLOADING SINGLE OBJECTS FROM A BUCKET ###
response = client.get_object(
    Bucket=bucket_name,
    Key=object_key,
)

# read in data from request
data = response['Body'].read()

# transform into pandas dataframe by reading in bytes
#df = pd.read_csv(io.BytesIO(data))

# print head
print(data.decode('utf-8'))