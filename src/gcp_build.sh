gcloud login
gcloud auth configure-docker northamerica-northeast1-docker.pkg.dev
docker build -t vlm-chat-cloud:latest -f src/Dockerfile .
docker tag vlm-chat-cloud:latest northamerica-northeast1-docker.pkg.dev/mlops-493703/vlm-chat-repo/vlm-chat-cloud:latest
docker push northamerica-northeast1-docker.pkg.dev/mlops-493703/vlm-chat-repo/vlm-chat-cloud:latest
