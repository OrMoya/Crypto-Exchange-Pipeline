# Crypto Data Pipeline with Python and AWS

![Arch](assets/images/arch_diagram.png)

## Overview
* Extracts and transform crypto data with Python from CoinCap Api 
* Data is loaded into AWS S3 and then transferred to an AWS RDS Postgres instance and then rendered by Metabase
* Python code runs on a schedule cron job through a virtual machine with AWS EC2

## How the Pipeline Works

### Tools 
| AWS  |
| ------------- | 
| RDS  | 
| S3  |
|EC2|
