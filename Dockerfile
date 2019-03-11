FROM python:3.7.2

#
# Meta information
#
LABEL description="Container with Workout portal API service"

#
# Internal params
#
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#
# Preparing of environment
#
WORKDIR /usr/src/app

# Add a launcher
ADD entrypoint.sh ./
RUN chmod +x ./entrypoint.sh

# Installation of dependencies
ADD ./requirements ./requirements
RUN pip install --no-cache-dir -r ./requirements/develop.txt

# Add a source code
ADD ./manage.py ./
ADD ./django_learning ./django_learning
ADD ./workout_portal ./workout_portal

# Removing of unused parts
RUN rm -rf ./requirements

## THE LIFE SAVER
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait

#
# Launcher
#
ENTRYPOINT ["./entrypoint.sh"]

CMD ["runserver", "0.0.0.0:8080"]

EXPOSE 8080
