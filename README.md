# Cybersecurity Intrusion Analysis

### Group Name
**Intrusions**

### Group Members
- Zena
- Ramon
- Amarylis
- Salman

## Problem Definition

The problem we are attempting to solve is pinpointing/summarizing identifying information regarding attempted hacks such as location, time, network, etc. We need data to help solve this problem because the more information we have on our attackers the better prepared we can be to prevent attempted intrusions going forward.

The questions guiding our analysis are:

- Where do most hack attempts come from?
- When do most hack attempts occur?
- What are signifying features of an attempted intrusion?

## Datasets

We began our analysis by reviewing an example dataset. This allowed us to practice our approach to Exploratory Data Analysis (EDA) and familiarize ourselves with key cybersecurity terms while our TKH honeypot collected the data necessary for our actual analysis.

## Setup

1. Pull repo into your work environment.
2. Setup a virtual environment this can be done using virtualenv.

```
pip install virtualenv
```

3. Activate the virtualenv (this will be different based on operating system not shown below) and install the dependencies for the project from requirements.txt in that environment to avoid conflicts.

``` bash
pip install -r requirements.txt
```


3. Create config.py which should contain aws credentials to access the S3 bucket. An example of what config.py should look like displayed below.

```
aws_access_key_id = "your-access-key-id"
aws_secret_access_key = "your-aws-secret-key"
```

Once set up the following codeblock will be able to execute provided that libraries are properly installed and view the merged_output.csv from the S3 bucket.


``` python

# some initial variables
bucket_name = "tkh-nyc-intrusions"
object_key = "merged_output.csv"

# open client
client = boto3.client('s3',
                      aws_access_key_id=config.aws_access_key_id,
                      aws_secret_access_key=config.aws_secret_access_key)

# retrieve objects in S3 bucket
response = client.get_object(
    Bucket=bucket_name,
    Key=object_key,
)

# read in data from request
data = response['Body'].read()

# transform into pandas dataframe by reading in bytes
df = pd.read_csv(io.BytesIO(data))

# print head
print(df)
```

