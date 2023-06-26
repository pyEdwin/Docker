####  Handcrafting a Container Image

<h6>Create a lightsail server</h6>

- Create a Lightsail server with Ubuntu OS

<h6> Get and Run the Base Image</h6>

* Get the httpd from docker hub
> docker pull htttpd:2.4

* Run the container
> docker run  --name web_template -d httpd:2.4 

* Check the container is running
> docker ps

* Log into the container to make change
> docker exec -it web_template bash

* Install Git 
> apt update && apt install git

* Clone a repository to web_template
>  git clone https://github.com/pyEdwin/web.git /temp/web_template

* Check the files
> ls -l /temp/web_factory

* Remove the index.html from apache
> rm /htdocs/index.html

* Remode README.md file
> rm /temp/web_factory/README.md

* Copy everything from web_factory to htdocs
> cp -r /temp/web_factory/* htdocs/

* List the files of htdocs
> ls -l htdocs

* Create two images from the container
> docker commit fef7c327ea37 web_template:v1
> docker commit fef7c327ea37 web_template:v2

* Delete the  web_taplate:v1 image
> docker rmi web_taplate:v1

* Run the image
> docker run -d --name web1 -p 8081:80 web_template:v2
> docker run -d --name web2 -p 8082:80 web_template:v2
> docker run -d --name web3 -p 8083:80 web_template:v2

* Stop a container
> docker stop w2