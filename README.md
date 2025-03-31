**OCRMyPDF on AWS ECS using Terraform

**Overview**

This project deploys OCRMyPDF on AWS ECS Fargate using Terraform. It enables PDF OCR processing using an EC2-hosted Python script that sends requests to AWS SQS, which triggers an ECS task to process the PDF.
Architecture

**EC2 Instance** – Runs a Python script that sends PDF processing requests to AWS SQS.

**AWS SQS** – Acts as a queue for PDF processing requests.

**ECS Fargate Task** – Runs OCRMyPDF in a container and processes messages from SQS.

**Prerequisites**

Terraform installed (Download)

AWS CLI configured (Guide)

Boto3 (Python SDK) installed: pip install boto3

**Deployment Steps**
**Clone the Repository**
git clone https://github.com/yourusername/OCRMyPDF-on-ECS.git
cd OCRMyPDF-on-ECS
**Initialize and Apply Terraform**
cd terraform
terraform init
terraform apply -auto-approve

This will create:

ECS Cluster and Task Definition

SQS Queue

EC2 Instance

Required IAM roles and policies

**Files and Directories**
OCRMyPDF-on-ECS/
│── terraform/          
│   ├── main.tf        
│   ├── variables.tf  
│   ├── outputs.tf     
│── scripts/          
│   ├── trigger_ocr.py
│── README.md         
│── .gitignore         
