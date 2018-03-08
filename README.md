# Project Title

This is a copy of the flask app I'm constructing

## Getting Started

Install Docker:
https://docs.docker.com/install/

An awesome tutorial is linked here:
https://docs.docker.com/get-started/#images-and-containers

### Quick and Dirty
The first good thing to understand is the difference between images and containers. Images are all the instructions your program needs to run, a container is that image running. Because the containers run natively on the hosts kernel, the containers are zippy and lightweight.

### Things to try starting out

Test your install:
```
docker run hello-world
```

### Cheat sheet for my image

After making the image, typically consisting of a program, the requirements for that program, and the Dockerfile, you build it with:
```
docker build -t imagename .
```

Once you have that built image you can run it, make the container, with:
```
docker run --name containername -d imagename #This is running the container in the backround and giving it a name
```

You can attach to your container to get a live feed with:
```
docker attach containername
```

You can disattach with Ctrl-C or Ctrl-D and restart the container with:
```
docker start conteinername
``` 

Or you can get a log of what your thing has been printing:
```
docker logs -f containername
```

Shutting down containers and removing them so that you can reuse the images:
```
docker stop containername
docker rm containername
```
