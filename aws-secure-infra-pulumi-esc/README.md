# 🛡️ Secure AWS Infrastructure Deployment using Pulumi ESC

This repository demonstrates how to **deploy AWS resources securely using Pulumi** (Infrastructure as Code) and **ESC (Environments, Secrets, and Configuration)** with **Python**.
It provisions **RDS, S3, and Security Groups** while securely managing credentials and passwords through Pulumi ESC.

---

## 🧩 Architecture Overview

```
                +-----------------------+
                |     Pulumi ESC        |
                |  (Secret Management)  |
                +----------+------------+
                           |
             +-------------+-------------+
             |                           |
     +-------v-------+           +-------v-------+
     |   AWS S3      |           |   AWS RDS     |
     | (Storage)     |           | (Database)    |
     +---------------+           +---------------+
             |                           |
             +-------------+-------------+
                           |
                   +-------v-------+
                   | Security Group |
                   | (Network Rules)|
                   +---------------+
```

---

## 🚀 Project Objective
Traditional IaC setups risk secret exposure and repetitive manual configuration.
This project eliminates those risks by combining:
- **Pulumi ESC** for secure secret storage.
- **Python modules** for modular infrastructure code.
- **Pulumi CLI** for end-to-end automation.

---

## 🧰 Prerequisites

Install and configure the following tools:

| Tool | Purpose |
|------|----------|
| Pulumi CLI | Manage IaC deployments |
| Python 3.x | Execute Pulumi scripts |
| pip | Manage Python packages |
| Git | Clone and version control |
| AWS CLI or Cloud9 | AWS environment configuration |

Optional: Use **AWS Cloud9** or any IDE like VSCode or PyCharm.

---

## ⚙️ Setup Instructions

1. **Create virtual environment and install deps**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Login and init stack**
   ```bash
   pulumi login
   pulumi stack init dev || true
   ```

3. **Export AWS credentials (if running locally)**
   ```bash
   export AWS_ACCESS_KEY_ID=<your-key>
   export AWS_SECRET_ACCESS_KEY=<your-secret>
   export AWS_DEFAULT_REGION=us-east-1
   ```

4. **Configure secrets with Pulumi**
   ```bash
   pulumi config set aws:region us-east-1
   pulumi config set aws-secure-infra-pulumi-esc:allowedCidr 0.0.0.0/0
   pulumi config set aws-secure-infra-pulumi-esc:dbPassword 'ChangeMe_S3cure!' --secret
   ```

5. **Preview and deploy**
   ```bash
   pulumi refresh
   pulumi preview
   pulumi up
   ```

6. **Retrieve outputs**
   ```bash
   pulumi stack output rdsEndpoint
   pulumi stack output bucketName
   pulumi stack output securityGroupId
   ```

**Sample Output:**
```bash
Outputs:
    bucketName: "secure-infra-bucket-1738"
    rdsEndpoint: "pulumi-rds.abcdefg1234.us-east-1.rds.amazonaws.com"
    securityGroupId: "sg-0abc123def456"
```

---

## 📂 Project Structure

```
aws-secure-infra-pulumi-esc/
│
├── infra/
│   ├── __init__.py
│   ├── rds.py                # Creates an RDS instance
│   ├── s3_bucket.py          # Creates an S3 bucket
│   └── security_group.py     # Defines inbound/outbound rules
│
├── main.py                   # Entry point importing infra modules
├── Pulumi.yaml               # Pulumi project definition
├── Pulumi.dev.yaml           # Stack configuration (includes secrets placeholder)
├── requirements.txt          # Project dependencies
├── .gitignore
└── README.md                 # Documentation
```

---

## 🧠 Troubleshooting

| Command | Description |
|----------|--------------|
| `pulumi refresh` | Sync Pulumi state with AWS |
| `pulumi logs -f` | Stream live logs |
| `pulumi destroy` | Tear down resources |
| `pulumi stack output` | Retrieve deployed resource info |

Common issues:
- **Provider conflicts:** reinstall AWS plugin  
  ```bash
  pulumi plugin install resource aws <version>
  ```
- **Access denied:** verify IAM user permissions for RDS, S3, and EC2.
- **Public access:** set `publicly_accessible=False` and restrict `allowedCidr` for production.

---

## 🧮 requirements.txt Example

```txt
pulumi
pulumi-aws
boto3
```

---

## 🌱 Future Enhancements
- Implement Pulumi Automation API for CI/CD integration.
- Add ECS (Elastic Container Service) for containerized workloads.
- Extend ESC configuration for multi-environment (dev/stage/prod) secrets management.
- Include automated test cases for infrastructure validation.

---

## 👨‍💻 Author

**Justin Haynes**  
Chief Operating Officer — Nexura Innovations  
🔗 LinkedIn: https://www.linkedin.com/in/justin-haynes/

---

## 📜 License
This project is licensed under the MIT License.
