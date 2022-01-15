# Devops
- Keyword for creating software.
    1. Enhance communication
    1. Automation 
    1. Quick Feedback

 ## Agile
 Focus on the __buisiness__ and __development__.
 ### Cycle
1. Code commit
1. Unit Tests
1. Code Quility
1. Package
1. Integration Tests

## Docker 
### Architecture
![Dodcker Architecture](https://1.bp.blogspot.com/-0cGTv60CHDs/XbLyudEldbI/AAAAAAAAM3k/RaJSzycNWNo68Lk6Q5Csf6B6pMw_k4IwQCLcBGAsYHQ/w1200-h630-p-k-no-nu/157.png)

### Docker Image Command
- `docker images` : List up docker images.
- `docker pull`: Pull images from the docker hub.
- `docker search` : Search image from the docker hub.
    - official[OK]: Confirmed officially.
- `docker image history`: Check the build layers.
- `docker image inspect` : Detail information about the image.


### Docker Container Command
- `docker pause container`: Pause the container.
    - `docker unpause container` : Resume the container.
- `docker stop container`: Stop (all processes running in the) container.
- `docker kill container`: Kill Immediatlly(Force kill all process).
- `docker inspect container`: See detailed information of the container.  
- `docker prone`: Remove all of the stopped containers.
- `docker run`: Run the container 
    - `-m` : Limit the memory
    - `--cpu-quota`: Limit the cpu(Total CPU Quota is 100,000).
    - `port_number_from_OS:port_number_from_container`
    - ex: `docker container run -p 5000:5000 -d -m 512m --cpu-quota=50000 in28min/hello-world-java:0.0.1.RELEASE`
- `docker stats container_id`: Check the status of the docker container. 
### Docker System Command 
- `docker system` : Docker system command
    - `df`: Show docker disk usage.
    - `events`: Get real time events from the server.
    - `prune`: Remove all of the unused data as the follows. 
        - containers: All the containers that are not used.
        - networks: All the networks that are not used. 
        - images: All the images that are not run by the contaner.
        - build-cache: The build cache that are not used.

### Dockerfile
Dockerfiles are text documents that allow you to build images for docker.
- `FROM python:alpine3.10`: Start from the specific base image.
- `WORKDIR /app` : Define working directory.
- `COPY . /app`: Copy all of the contents in current dir to /app.
- `RUN pip install -r requirements.txt`
- `EXPOSE 5000`:  Expose the specific port.
- `CMD python ./launch.py`: Excute the command.

The difference between `RUN`, `CMD`, `ENTRYPOINT`
- `RUN`: Adding layers when build the docker container, using for installing libs and apps.
- `CMD`: The default command to run after the container build up, The arguments will be replaced, if user pass the arguments after the `docker run`.
- `ENTRYPOINT`: The must run command after the container build up. The arguments will not be replaced. 

#### Dockerfile example 01:
- Docker file: [Dockerfile](01_build_up_first_image/Dockerfile)

```shell
# Building image
docker build -t qianlin725/hello-world-python:0.0.1.RELEASE .

# Run the container
docker run -p 3000:3000 -d qianlin725/hello-world-python:0.0.1.RELEASE
```