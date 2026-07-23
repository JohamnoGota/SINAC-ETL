terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 6.0"
    }
  }
}

provider "aws"{
    # configure the options
    region = "mx-central-1"
}

# Create a simple S3 bucket 
resource "aws_s3_bucket" "tf_test_bucket_johamno"{
    bucket = "johamno-tf-test-bucket"
    tags = {
        Name    = "My bucket 1234"
        Environment = "Dev"
    }
}