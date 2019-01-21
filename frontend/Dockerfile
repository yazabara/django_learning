FROM node:10-alpine

#
# Meta information
#
LABEL description="Container with Workout Portal UI"

#
# Preparing of environment
#
WORKDIR /usr/src/app/frontend

# Installation of dependencies
ADD ./package.json ./package-lock.json ./
RUN npm install && npm cache clean --force

# Add a source code
ADD ./angular.json ./tsconfig.json ./
ADD ./src ./src

# Add a launcher
ADD ./entrypoint.sh ./
RUN chmod +x ./entrypoint.sh

#
# Launcher
#
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 4200
