# 🚀 Multi API Serverless ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange?style=for-the-badge&logo=awslambda)
![Amazon S3](https://img.shields.io/badge/Amazon-S3-red?style=for-the-badge&logo=amazons3)
![DynamoDB](https://img.shields.io/badge/Amazon-DynamoDB-blue?style=for-the-badge&logo=amazondynamodb)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-black?style=for-the-badge&logo=githubactions)

---

## 📌 Project Overview

Multi API Serverless ETL is an AWS-based event-driven data pipeline that automatically collects data from multiple public APIs, stores raw JSON files in Amazon S3, processes them using AWS Lambda, and saves the transformed data into Amazon DynamoDB.

The project follows a serverless architecture, making it scalable, lightweight, and easy to maintain.

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
