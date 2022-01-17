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
    - `--link`: Connect link via two containers.
    - `--network`: Connect the containers to specific docker network(bridge).
        - `docker network create docker_network_name`
    - `--env`: Setting environment variables for the target container.
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

### The difference between `RUN`, `CMD`, `ENTRYPOINT`
- `RUN`: Adding layers when build the docker container, using for installing libs and apps.
- `CMD`: The default command to run after the container build up, The arguments will be replaced, if you pass the command line arguments after the `docker run`.
- `ENTRYPOINT`: The must run command after the container build up. The arguments will not be replaced. 

#### Dockerfile example 01:
- Docker file: [Dockerfile](01_build_up_first_image/Dockerfile)

```shell
# Building image
docker build -t qianlin725/hello-world-python:0.0.1.RELEASE .

# Run the container
docker run -p 3000:3000 -d qianlin725/hello-world-python:0.0.1.RELEASE
```

- Note: building java require two stage build up.
    - first stage: Use maven to build jar file.
    - second stage: Use jar file to call REST API.


### Push Images to the Dockerhub
1. Make an account from [dockerhub](https://hub.docker.com/).
1. `docker login` from your terminal.
1. Push your image by running command `docker push image_name:tag_info`.

### How to make efficient images?
- Put the layers(cache) change sensitively to the bottom. 
    - All the layers located at the bottom of the changed layer will build as a new layer.

### Docker and Microservices
#### Microsercies
- Definition: 
    - > Small autonomous services that work together. - __Sam Newman__.
    - > In short, the microservice architectural style is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API. These services are built around business capabilities and are independently deployable by fully automated deployment machinery. There is a bare minimum of centralized management of these services, which may be written in different programming languages and use different data storage technologies. - __James Lewis and Martin Flowler__.

- Features:
    - Exposed by REST. 
    - Small Well Chosen Deplyable Units.
    - Cloud Enabled.

- Advantages: 
    - Flexibility: Easily adapt new technology and process.
    - Dynamic scaling: Dynamically scale up and scale down by occasions.
    - Faster release cycles: Fast deployment to the market.

### Docker with microservices can provide flexibility
- Easier development
    - Adopt new technology faster.
        - Zero worry about deployment procedures.
    - Fewer environmental issues.
        - No more - "It works only in my local."
- Easier operations
    - Consistent deployment automation across different environments and different technologies.

#### Example: Connect two micro service containers.
```shell
# Currency-exchange microservice: The service provide exchange EUR to INR
docker run -p 8000:8000 --name=currency-exchange -t in28min currency-exchange:0.0.1-RELEASE

# Currency-exchange microservice: The service provide quantity calculation.
# Need to be connected to the currency-exchange container, and set env variable CURRENCY_EXCHANGE_SERVICE_HOST.
docker run -d -p 8100:8100 --name=currency-conversion --link currency-exchange --env CURRENCY_EXCHANGE_SERVICE_HOST=http://currency-exchange  in28min/currency-conversion:0.0.1-RELEASE
```

### Docker compose
> Compose is a tool for defining and running multi-container Docker applications. - From Docker docs.
    - Use [YAML](https://yaml.org/) file : [docker-compose.yml](02_docker_compose/docker-compose.yml)

- YAML Example
```yaml
# First Docker Compose Example
version: 1.0
services:
  currency-exchange: 
    image: in28min/currency-exchange:0.0.1-RELEASE
    ports:
      - "8000:8000"
    restart: always
    networks:
      - currency-compose-network
  
  currency-conversion:
    image: in28min/currency-conversion:0.0.1-RELEASE
    ports:
      - "8100:8100"
    restart: always
    environment:
      CURRENCY_EXCHANGE_SERVICE_HOST: http://currency-exchange
    depends_on:
      - currency-exchange
    networks:
      - currency-compose-network
networks:
  currency-compose-network:
```

- Running Command for docker-compose: 
    - Run interactively: `docker-compose up`
    - Shut down docker compose: `docker-compose down`
    - Run background(detach mode):
        ```shell
        docker-compose up -d
        docker-compose logs
        ```
    - Check compose: `docker-compose ps`
    - Check validation: `docker-compose config`
    - pause, unpause, stop, kill, top etc


