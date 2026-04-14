docker build -t ssunku6/vlm-chat-cloud:latest -f src/Dockerfile .
docker push ssunku6/vlm-chat-cloud:latest
docker run -p 22011:22011 --env-file src/.env ssunku6/vlm-chat-cloud:latest