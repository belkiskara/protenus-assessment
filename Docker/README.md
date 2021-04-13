
# NGINX webserver that serves a simple page containing its hostname, IP address and port as wells as the request URI and the local time of the webserver.

This repository created base on NGiNX Docker sample from -- https://hub.docker.com/r/nginxdemos/hello/.


How to run:
```
$ docker build .
$ docker tag #GeneratedDockerID nginxdemo
$ docker run -P -d nginxdemo
```

You tag the docker tag # ImageID # as theTag you want to give.

If you run the docker run as the Tag you want, it works with the default port, 80.

With specified port: 
```
$ docker run -p 8081:80 -d nginxdemo
```
Now, assuming we found out the IP address and the port that mapped to port 80 or specified port on the container, in a browser we can make a request to the webserver and get the periodic table generated based on html tags.

You can name it with the -n parameter to name it. While killing it makes your job easier, but optional, so there is no need.

to stop;

```
$ curl <ip>:<port>
Server address: 172.17.0.2:80
Server name: 22becba5323d
Date: 07/Feb/2018:16:05:05 +0000
URI: /
Request ID: 48ba0db334a6ed165e783469c2af868f
```

How to clean container and image
```
$ docker build .
$ docker tag #GeneratedDockerID nginxdemo
$ docker run -P -d nginxdemo
```

You write docker ps, you get containerID from the list
```
$ docker ps
```
If you type docker kill containerID, the process stops
```
$ docker kill nginxdemo #Name of Container
$ docker kill #GeneratedContainerID
```
If you type docker rm containerID, the Container will be deleted

```
$ docker rm nginxdemo #Name of Container
$ docker rm #GeneratedContainerID
```

If you type theTag you want to give docker rmi, the image will be deleted.

```
$ docker rmi nginxdemo #Name of Container
$ docker rmi #GeneratedContainerID
```
To delete both container and image directly

If you do the Tag --force you want to give the docker rmi, it will clear all of them.

```
$ docker rmi nginxdemo --force #Name of Container
$ docker rmi #GeneratedContainerID --force
```
