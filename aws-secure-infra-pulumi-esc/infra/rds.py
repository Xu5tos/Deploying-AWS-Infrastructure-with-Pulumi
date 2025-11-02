import pulumi
import pulumi_aws as aws
from pulumi import Config

from .security_group import security_group

config = Config()

# Secret: database password managed by Pulumi config (ESC)
db_password = config.require_secret("dbPassword")

# Discover default VPC and subnets for a simple demo deployment
vpc = aws.ec2.get_vpc(default=True)
subnets = aws.ec2.get_subnets(filters=[aws.ec2.GetSubnetsFilterArgs(name="vpc-id", values=[vpc.id])])

# Subnet group for RDS across the default VPC subnets
subnet_group = aws.rds.SubnetGroup(
    "rds-subnet-group",
    subnet_ids=subnets.ids,
    tags={"Name": "pulumi-rds-subnet-group"},
)

# Parameter group (optional; using default engine family here)
param_group = aws.rds.ParameterGroup(
    "rds-param-group",
    family="postgres14",
    parameters=[],
    tags={"Name": "pulumi-rds-params"},
)

# Create a small Postgres RDS instance (public for demo; restrict in production)
rds_instance = aws.rds.Instance(
    "pulumi-postgres",
    engine="postgres",
    engine_version="14",
    instance_class="db.t3.micro",
    allocated_storage=20,
    db_subnet_group_name=subnet_group.name,
    vpc_security_group_ids=[security_group.id],
    username="pulumi",
    password=db_password,
    skip_final_snapshot=True,
    publicly_accessible=True,  # For demo; set False in production
    deletion_protection=False,
    apply_immediately=True,
    parameter_group_name=param_group.name,
    tags={
        "Name": "pulumi-postgres",
        "Environment": "dev",
    },
)

# Export values used by main.py
rds_endpoint = rds_instance.address
