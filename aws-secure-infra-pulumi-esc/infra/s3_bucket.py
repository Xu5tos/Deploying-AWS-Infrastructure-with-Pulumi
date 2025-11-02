import pulumi
import pulumi_aws as aws

# Create an S3 bucket with a unique prefix and auto-destroy enabled for demo use
bucket = aws.s3.BucketV2(
    "secure-infra-bucket",
    force_destroy=True,
    tags={
        "Project": "pulumi-esc-secure-infra",
        "ManagedBy": "Pulumi",
    },
)

bucket_name = bucket.bucket
