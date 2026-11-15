# Step-by-Step Guide (run all commands in the VS Code terminal: Ctrl + `)

## 0. Prerequisites
- Install VS Code, Docker Desktop, Git
- Docker Desktop -> Settings -> Kubernetes -> Enable Kubernetes -> Apply & Restart
- VS Code extensions: Docker, Kubernetes, YAML (Red Hat), Python

Verify (screenshot this):
    docker --version
    kubectl version --client
    kubectl get nodes        # STATUS must be Ready

## 1. (Optional) Test the app without Docker
    pip install -r requirements.txt
    python app.py            # open http://localhost:5000, then Ctrl+C

## 2. Build the Docker image
    docker build -t flask-k8s-demo:v1 .
    docker images

## 3. Run in a container
    docker run -d -p 5000:5000 --name flask-demo flask-k8s-demo:v1
    docker ps
    docker logs flask-demo
    # open http://localhost:5000
    docker stop flask-demo
    docker rm flask-demo

## 4. Deploy to Kubernetes
    kubectl apply -f k8s/
    kubectl get deployments
    kubectl get pods -o wide
    kubectl get svc
    kubectl describe deployment flask-demo

Open the app:
- Docker Desktop: http://localhost:30007
- Minikube:  minikube image load flask-k8s-demo:v1   (before applying)
             minikube service flask-demo-service
- kind:      kind load docker-image flask-k8s-demo:v1  (before applying)
             kubectl port-forward svc/flask-demo-service 8080:80  -> http://localhost:8080

Refresh the page several times: the pod name changes (load balancing).

## 5. Cloud-native features (show in demo)
Scaling:
    kubectl scale deployment flask-demo --replicas=5
    kubectl get pods

Self-healing:
    kubectl get pods
    kubectl delete pod <one-pod-name>
    kubectl get pods -w        # a new pod appears automatically (Ctrl+C to exit)

Rolling update:
    docker build --build-arg APP_VERSION=v2 -t flask-k8s-demo:v2 .
    kubectl set image deployment/flask-demo flask-demo=flask-k8s-demo:v2
    kubectl rollout status deployment/flask-demo
    # refresh browser: version shows v2
    kubectl rollout history deployment/flask-demo
    kubectl rollout undo deployment/flask-demo    # back to v1

Logs / debugging:
    kubectl logs <pod-name>
    kubectl describe pod <pod-name>

## 6. (Optional) Push to Docker Hub
    docker login
    docker tag flask-k8s-demo:v1 YOUR_USERNAME/flask-k8s-demo:v1
    docker push YOUR_USERNAME/flask-k8s-demo:v1
Then change `image:` in k8s/deployment.yaml to YOUR_USERNAME/flask-k8s-demo:v1

## 7. Screenshots to save in /screenshots
1. docker --version, kubectl get nodes
2. docker build output
3. docker images + docker ps
4. App in browser (Docker container)
5. kubectl apply -f k8s/
6. kubectl get pods, deployments, svc
7. App in browser via NodePort (30007)
8. Scaling to 5 replicas
9. Pod deleted and recreated
10. Rolling update and rollback

## 8. Push to GitHub
Create an EMPTY repo on github.com (e.g. flask-k8s-demo), then:
    git init
    git add .
    git commit -m "Docker and Kubernetes assignment"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/flask-k8s-demo.git
    git push -u origin main

## 9. Clean up after recording
    kubectl delete -f k8s/
