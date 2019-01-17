rem Stop all containers
docker stop $(docker ps -a -q)

rem Delete all containers
docker rm $(docker ps -a -q)

rem Delete all images
docker rmi $(docker images -a -q)