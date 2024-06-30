import boto3
import pandas as pd
import io

# AWS credentials (assumes credentials are set in the environment or using IAM roles)
s3 = boto3.client('s3')

# Function to merge all CSV files in an S3 bucket
def merge_csv_files(bucket_name, output_file):

    data_frames = []
    
    # List objects in the specified S3 bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Filter for CSV files
    csv_files = [content['Key'] for content in response.get('Contents', []) if content['Key'].endswith('.csv')]

    # Download and read each CSV file into a DataFrame
    for file_key in csv_files:
        csv_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        csv_data = csv_obj['Body'].read().decode('utf-8')
        data_frame = pd.read_csv(io.StringIO(csv_data), low_memory=False)
        data_frames.append(data_frame)

    # Concatenate all DataFrames
    merged_data = pd.concat(data_frames, ignore_index=True)

    # Convert the merged DataFrame back to CSV
    csv_buffer = io.StringIO()
    merged_data.to_csv(csv_buffer, index=False)

    # Upload the merged CSV back to S3
    s3.put_object(Bucket=bucket_name, Key=output_file, Body=csv_buffer.getvalue())

# Example usage
bucket_name = 'tkh-nyc-intrusions'
output_file = 'merged_output_test.csv'
merge_csv_files(bucket_name, output_file)