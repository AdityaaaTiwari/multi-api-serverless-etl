# 🚀 Multi API Serverless ETL Pipeline

> An event-driven ETL pipeline built with AWS that automatically processes data from multiple public APIs using Amazon S3, AWS Lambda, and DynamoDB.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?style=for-the-badge&logo=awslambda)
![Amazon S3](https://img.shields.io/badge/Amazon-S3-569A31?style=for-the-badge&logo=amazons3)
![Amazon DynamoDB](https://img.shields.io/badge/Amazon-DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb)
![CloudWatch](https://img.shields.io/badge/Amazon-CloudWatch-FF4F8B?style=for-the-badge&logo=amazoncloudwatch)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?style=for-the-badge&logo=githubactions)

---

## 📖 Overview

This project demonstrates a **serverless ETL (Extract, Transform, Load) pipeline** on AWS.

Data is collected from multiple public APIs, uploaded to **Amazon S3**, automatically processed by **AWS Lambda**, and stored in **Amazon DynamoDB**. The entire workflow is event-driven, meaning the pipeline starts automatically whenever a new JSON file is uploaded to S3.

The project is modular, scalable, and easy to extend by adding new APIs and processing Lambdas.

---

## 🎯 Project Objective

The objective of this project is to build a fully automated ETL (Extract, Transform, Load) pipeline using AWS services without managing any servers.

Instead of manually processing data, the system automatically detects uploaded files, routes them to the correct processing Lambda, transforms the data, and stores it in DynamoDB.

---

# 🏗️ Architecture

```

                 Public APIs
                       │
                       ▼
            Python Fetch Scripts
                       │
                       ▼
                  Amazon S3
                       │
              Object Created Event
                       │
                       ▼
                Router Lambda
          ┌────────┼────────┬────────┐
          ▼        ▼        ▼        ▼
      Weather  Earthquake Product Transit
        Lambda    Lambda    Lambda   Lambda
          │         │         │         │
          ▼         ▼         ▼         ▼
       DynamoDB  DynamoDB  DynamoDB  DynamoDB
                       │
                       ▼
                 CloudWatch Logs

```

---

# ⚙️ Workflow

### Step 1

Python scripts fetch data from different public APIs.

- Weather API
- Earthquake API
- Product API
- Transit API

---

### Step 2

The fetched JSON files are uploaded to Amazon S3.

Example:

```

weather/weather.json
earthquake/earthquake.json
product/product.json
transit/transit.json

```

---

### Step 3

Amazon S3 automatically triggers the Router Lambda.

---

### Step 4

The Router Lambda checks which folder the uploaded file belongs to and invokes the correct processing Lambda.

Example

```

weather/ → Weather Lambda
product/ → Product Lambda

```

---

### Step 5

The processing Lambda:

- Reads the JSON
- Validates required fields
- Transforms the data
- Stores it in DynamoDB

---

### Step 6

CloudWatch stores execution logs for monitoring and debugging.

---

# ✨ Features

- Event-driven architecture
- Serverless ETL pipeline
- Automatic S3 triggers
- Router Lambda for intelligent routing
- Modular Python code
- Shared utility functions
- CloudWatch logging
- DynamoDB integration
- GitHub Actions CI
- Easy to extend with new APIs

---

# ☁️ AWS Services Used

| Service | Purpose |
|----------|---------|
| Amazon S3 | Store raw JSON files |
| AWS Lambda | Process uploaded files |
| Amazon DynamoDB | Store processed data |
| Amazon CloudWatch | Logs and monitoring |
| IAM | Permissions and security |

---

# 📂 Project Structure

```

multi-api-serverless-etl

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
├── diagrams/
├── docs/
├── infra/
│
├── lambdas/
│   ├── weather/
│   ├── earthquake/
│   ├── product/
│   ├── transit/
│   └── router/
│
├── scripts/
├── shared/
├── tests/
│
├── requirements.txt
├── buildspec.yml
├── README.md
└── .gitignore

```

---

# 🛠️ Tech Stack

- Python
- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon CloudWatch
- Git
- GitHub
- GitHub Actions

---

# 🚀 How to Run

1. Clone the repository.

```

git clone <repository-url>

```

2. Install dependencies.

```

pip install -r requirements.txt

```

3. Run fetch scripts.

```

python scripts/weather_fetch.py

```

4. Upload generated JSON files to S3.

5. The pipeline will automatically process the data.

---

# 📊 Sample Output

### Weather Table

| Timestamp | Temperature | Humidity |
|------------|-------------|----------|
| 2026-07-02T... | 26°C | 71% |

---

### Product Table

| Product | Category | Price |
|----------|----------|-------|
| Essence Mascara | Beauty | 9.99 |

---

### Earthquake Table

| Magnitude | Place |
|------------|-------|
| 2.4 | Alaska |

---

### Transit Table

| Stop | Municipality |
|------|--------------|
| 13818 | Weymouth |

---

# 📸 Project Screenshots

Add screenshots here:

- S3 Bucket
- Lambda Functions
- Router Lambda
- CloudWatch Logs
- DynamoDB Tables
- GitHub Actions

---

# 🔮 Future Improvements

- API Gateway Integration
- SNS Notifications
- AWS Step Functions
- Infrastructure as Code (Terraform / CloudFormation)
- Monitoring Dashboard
- Data Analytics Dashboard

---

# 👨‍💻 Author

**Aditya Tiwari**

B.Tech CSE Student

AWS | Python | Data Engineering | Cloud Computing
