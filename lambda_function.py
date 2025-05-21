import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    for record in event.get('Records', []):
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        try:
            print(f"Checking tags for object: {key} in bucket: {bucket}")
            response = s3.get_object_tagging(Bucket=bucket, Key=key)
            tags = {tag['Key']: tag['Value'] for tag in response.get('TagSet', [])}

            if not tags or 'Name' not in tags:
                print(f"Object {key} has no tags or missing 'Name' tag. Deleting...")
                s3.delete_object(Bucket=bucket, Key=key)
                print(f"Deleted object: {key}")
            else:
                print(f"Object {key} has valid tags. No action taken.")

        except Exception as e:
            print(f"Error processing {key}: {e}")
            continue

    return {
        'statusCode': 200,
        'body': 'Checked and deleted untagged files if needed.'
    }
