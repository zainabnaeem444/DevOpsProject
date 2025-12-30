\# Docker Job Documentation



\*\*Owner:\*\* Zainab  

\*\*Purpose:\*\* Containerization and orchestration of EcoMetrics application



---



\## Overview



The Docker Job is responsible for:

\- Creating Dockerfiles for receiver and sender services

\- Orchestrating with Docker Compose

\- Deploying to Kubernetes (Minikube)

\- Publishing images to DockerHub



---



\## Files Created



\### Docker Files

\- `Dockerfile.receiver` - Container for Taipy dashboard

\- `Dockerfile.sender` - Container for data generator

\- `docker-compose.yml` - Local multi-container orchestration

\- `.dockerignore` - Exclude unnecessary files from images



\### Kubernetes Manifests

\- `k8s/base/namespace.yaml` - ecometrics namespace

\- `k8s/base/configmap.yaml` - Configuration management

\- `k8s/base/receiver-deployment.yaml` - Receiver pod deployment

\- `k8s/base/receiver-service.yaml` - Expose receiver service

\- `k8s/base/sender-deployment.yaml` - Sender pod deployment



\### Modified Files

\- `src/receiver.py` - Added environment variable support, fixed host binding

\- `src/sender.py` - Added connection delay and environment variables



---



\## DockerHub Images



Published at:

\- `zainabnaeem/ecometrics-receiver:latest`

\- `zainabnaeem/ecometrics-sender:latest`



---



\## Running Locally



\### Docker Compose

```bash

docker-compose up

```

Access: http://localhost:5000



\### Kubernetes (Minikube)

```bash

minikube start

kubectl apply -f k8s/base/

minikube service receiver-service -n ecometrics

```



---



\## Architecture

```

Sender Container  ──socket──>  Receiver Container

&nbsp;                                   │

&nbsp;                                   ├─ Port 5000 (Web UI)

&nbsp;                                   └─ Port 65432 (Socket)

```



---



\## Key Challenges \& Solutions



\*\*Challenge 1:\*\* Sender connecting before receiver ready  

\*\*Solution:\*\* Added 10-second delay in sender.py



\*\*Challenge 2:\*\* Taipy binding to 127.0.0.1 in container  

\*\*Solution:\*\* Changed to host="0.0.0.0" in gui.run()



\*\*Challenge 3:\*\* Pickle data truncation  

\*\*Solution:\*\* Implemented buffering in receiver socket handler



\*\*Challenge 4:\*\* YAML tab characters  

\*\*Solution:\*\* Used spaces-only indentation



---



\## Deliverables Checklist



\- \[x] Dockerfile.receiver created

\- \[x] Dockerfile.sender created

\- \[x] docker-compose.yml created

\- \[x] Kubernetes manifests created

\- \[x] Docker Compose tested locally

\- \[x] Deployed to Minikube successfully

\- \[x] Images pushed to DockerHub

\- \[x] K8s using DockerHub images tested

\- \[x] Documentation complete



---



\*\*Docker Job Status:\*\*  Complete  

\*\*Total Time:\*\* 6-7 hours  

\*\*Images:\*\* Available on DockerHub for deployment

