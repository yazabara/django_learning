@echo off
docker-compose -f ../frontend/ui-docker-compose.yml -f ../api-docker-compose.yml %*