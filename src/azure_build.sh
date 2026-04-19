az login
az acr login --name vlmchatregistry
docker buildx build --platform linux/amd64 --provenance=false -t vlmchatregistry.azurecr.io/vlm-chat-cloud:v2 --push -f src/Dockerfile .