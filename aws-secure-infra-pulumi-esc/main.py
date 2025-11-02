import pulumi
from infra.rds import rds_endpoint
from infra.s3_bucket import bucket_name
from infra.security_group import security_group_id

# Export key outputs for convenient access
pulumi.export("bucketName", bucket_name)
pulumi.export("rdsEndpoint", rds_endpoint)
pulumi.export("securityGroupId", security_group_id)
