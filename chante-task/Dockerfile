FROM alpine:latest 


RUN apk --update add python3

# Copies the files to / dir in image
COPY src/code /

# Executes python3 with /opt/hello-docker.py as the only parameter
ENTRYPOINT ["python3","test.py"]