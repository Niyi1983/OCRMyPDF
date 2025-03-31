import boto3
import json

sqs = boto3.client("sqs", region_name="us-east-1")
QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/123456789012/ocr-processing-queue"

pdf_details = {"bucket": "my-pdf-bucket", "file": "sample.pdf"}
response = sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps(pdf_details))
print(f"Message sent to SQS: {response['MessageId']}")
