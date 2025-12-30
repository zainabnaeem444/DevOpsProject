# Deployment Job Documentation
**Owner:** Fatima
**Status:** Dashboard Live on AWS

## Infrastructure Overview
- [cite_start]**Provider:** AWS EC2 (Amazon Linux 2023) [cite: 350]
- [cite_start]**Instance Type:** t3.micro [cite: 350]
- **Public IP:** [Public EC2 IP]

## Network Configuration (Security Groups)
The following inbound rules were configured to allow traffic:
- [cite_start]**Port 22:** SSH access [cite: 350]
- [cite_start]**Port 5000:** Taipy Dashboard UI
- [cite_start]**Port 65432:** Real-time data socket connection

## Deployment Steps
1. [cite_start]Docker and Docker Compose installed on EC2[cite: 351].
2. [cite_start]Pulling images from DockerHub: `zainabnaeem/ecometrics-receiver`[cite: 333, 351].
3. [cite_start]Running containers in detached mode: `docker-compose up -d`.

## Test Dashboard 
1. AWS console -> EC2 -> Ecometrics Server -> Security Groups -> launch wizard -> Edit Inbound rules 
2. Add Rule: 
Type: Custom TCP 
Port: 5000 
Source: MyIP