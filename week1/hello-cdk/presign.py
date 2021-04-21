import boto3

url = boto3.client('s3').generate_presigned_url(
ClientMethod='get_object', 
Params={'Bucket': 'shakemates-applications', 'Key': 'MOCK_DATA.csv'},
ExpiresIn=120)

print(url)