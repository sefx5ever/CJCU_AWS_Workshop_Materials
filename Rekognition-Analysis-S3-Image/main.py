import boto3

def lambda_handler(event,context):
    bucket = event['Records'][0]['s3']['bucket']['name'] # S3 Bucket 的 Name
    photo = event['Records'][0]['s3']['object']['key'] # 
    model = ''
    min_confidence = 90
    return show_custom_labels(model,bucket,photo,min_confidence)

def show_custom_labels(model,bucket,photo,min_confidence):
    client = boto3.client('rekognition')

    # Call DetectCustomLabels
    return client.detect_custom_labels(
        ProjectVersionArn = model,
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxResults = 1,
        MinConfidence = min_confidence
    )
