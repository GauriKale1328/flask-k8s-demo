# Demo Recording Script (about 8-10 minutes)

Record with Zoom / Google Meet / Teams / OBS. Share your whole screen (VS Code + browser).

1. **Intro (30s)** - Name, PRN/roll no, topic: "Containerizing a Flask app with Docker and deploying on Kubernetes".
2. **Project tour (1 min)** - Show files in VS Code: app.py, Dockerfile, k8s/deployment.yaml, k8s/service.yaml, GitHub repo.
3. **Dockerfile (1.5 min)** - Explain each instruction: FROM, ARG/ENV, WORKDIR, COPY requirements first (layer caching), RUN pip install, EXPOSE, CMD.
4. **Build and run (1.5 min)** - docker build, docker images, docker run, docker ps, open localhost:5000.
5. **Kubernetes YAML (2 min)**
   - Deployment: replicas, selector/labels, template, image, probes, resources, rolling update strategy.
   - Service: NodePort, port 80 -> targetPort 5000, selector matches pod labels.
6. **Deploy (1.5 min)** - kubectl apply -f k8s/, get pods / deployments / svc, open http://localhost:30007, refresh to show pod names changing.
7. **Cloud-native features (2 min)** - Scale to 5, delete a pod (self-healing), rolling update to v2, rollback.
8. **Concepts summary (1 min)** - Say these terms:
   - Container vs VM, image vs container
   - Pod, ReplicaSet, Deployment, Service, labels and selectors
   - Declarative configuration (desired state)
   - Scalability, self-healing, rolling updates, rollback
   - Health probes, resource requests/limits
   - Portability: same manifests run on EKS / AKS / GKE
   - Microservices and cloud-native principles
9. **Close (15s)** - Mention GitHub link and thank the evaluator.

Upload the video (Google Drive / YouTube unlisted) and paste the link in README.md.
