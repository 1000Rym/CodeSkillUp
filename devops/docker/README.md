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