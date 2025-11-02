import pulumi
import pulumi_aws as aws
from pulumi import Config

config = Config()

# Get the default VPC (adjust if you want a specific VPC)
default_vpc = aws.ec2.get_vpc(default=True)

# Allow list (CIDR) for inbound DB access; default is 0.0.0.0/0 for demo only
allowed_cidr = config.get("allowedCidr") or "0.0.0.0/0"

security_group = aws.ec2.SecurityGroup(
    "db-security-group",
    description="Security group for RDS allowing inbound DB access",
    vpc_id=default_vpc.id,
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=5432,
            to_port=5432,
            cidr_blocks=[allowed_cidr],
            description="Allow PostgreSQL from allowed CIDR",
        )
    ],
    egress=[
        aws.ec2.SecurityGroupEgressArgs(
            protocol="-1",
            from_port=0,
            to_port=0,
            cidr_blocks=["0.0.0.0/0"],
            ipv6_cidr_blocks=["::/0"],
            description="Allow all outbound",
        )
    ],
    tags={"Name": "pulumi-db-sg"},
)

security_group_id = security_group.id
