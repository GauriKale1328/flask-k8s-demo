# Docker and Kubernetes Deployment - Cloud-Native Assignment

**Name:** Gauri Kale
**PRN / Roll No:** 202301040079
**Course:** Cloud Computing / Cloud-Native

## Overview
A simple Flask web app containerized with Docker and deployed to Kubernetes
with a Deployment (3 replicas) and a NodePort Service. The page shows the pod
name serving each request, which demonstrates load balancing.

## Project structure
```
flask-k8s-demo/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── screenshots/
├── STEPS.md
├── DEMO_SCRIPT.md
└── README.md
```

## Run with Docker
```bash
docker build -t flask-k8s-demo:v1 .
docker run -d -p 5000:5000 --name flask-demo flask-k8s-demo:v1
```
Open http://localhost:5000

## Deploy on Kubernetes
```bash
kubectl apply -f k8s/
kubectl get pods
kubectl get svc
```
Open http://localhost:30007

## Cloud-native features demonstrated
- Scaling: `kubectl scale deployment flask-demo --replicas=5`
- Self-healing: delete a pod and a new one is created
- Rolling update and rollback: `kubectl set image ...` / `kubectl rollout undo ...`
- Health probes and resource limits

## Screenshots
Add images from the `screenshots/` folder here.

## Demo video
PASTE VIDEO LINK HERE

## Technologies
Python, Flask, Docker, Kubernetes, kubectl, GitHub
