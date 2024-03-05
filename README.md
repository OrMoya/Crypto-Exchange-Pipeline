# Crypto Data Pipeline with Python and AWS

![Arch](assets/images/arch_diagram.png)

## Overview
* Extracts and transform crypto data with Python from CoinCap Api 
* Data is loaded into AWS S3 and then transferred to an AWS RDS Postgres instance and then rendered by Metabase
* Python code runs on a scheduled Cloudwatch event which trigger AWS Lambda function call every 5 minutes

## How the Pipeline Works

### Tools  
| AWS  | API | Visualization |
| -----|------- | ----- |
| RDS  | CoinCap | Metabase|
| S3  | | Docker |
|EC2| | |
|Lambda| | |
